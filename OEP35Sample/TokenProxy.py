from ontology.libont import AddressFromVmCode, bytes2hexstring, bytearray_reverse
from ontology.interop.Ontology.Native import Invoke
from ontology.interop.Ontology.Runtime import Base58ToAddress
from ontology.builtins import bytearray, hash160, Exception, state
from ontology.interop.System.Storage import Put, GetContext, Get, Delete
from ontology.interop.System.App import RegisterAppCall, DynamicAppCall
from ontology.interop.System.ExecutionEngine import GetExecutingScriptHash
from ontology.interop.System.Runtime import CheckWitness, Notify, Serialize, Deserialize, GetTime

####################################
ctx = GetContext()
ContractAddress = GetExecutingScriptHash()
Admin = Base58ToAddress('AGjD4Mo25kzcStyh1stp7tXkUuMopD43NT')
ONTAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
ONGAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02')

#################Prefix Setting####################
TOKEN_SYMBOL_PREFIX = 'TOKEN_SYMBOL'
TOKEN_HASH_PREFIX = 'TOKEN_HASH'
SUPPORTED_TOKEN = 'SUPPORTED_TOKEN'
REGISTERED_EXCHANGE = 'REGISTERED_EXCHANGE'
EXCHANGE_ID_PREFIX = "EXCHANGE_ID"
EXCHANGE_NAME_PREFIX = "EXCHANGE_NAME"

def Main(operation, args):

    if operation == "AddToken":
        symbol = args[0]
        hash = args[1]
        return AddToken(symbol, hash)

    if operation == "RemoveToken":
        symbol = args[0]
        hash = args[1]
        return RemoveToken(symbol, hash)

    if operation == "GetTokens":
        return GetTokens()

    if operation == "RegisterExchange":
        exchangeName = args[0]
        exchangeId = args[1]
        return RegisterExchange(exchangeName, exchangeId)

    if operation == "RemoveExchange":
        exchangeName = args[0]
        exchangeId = args[1]
        return RemoveExchange(exchangeName, exchangeId)

    if operation == "GetAuthorizedExchange":
        return GetAuthorizedExchange()

    # if operation == "Approve":
    #     return Approve()
    #
    # if operation == "Allowance":
    #     return Allowance()

    if operation == "TokenTransferFrom":
        exchangeId = args[0]
        order = args[1]
        return TokenTransferFrom(exchangeId, order)

    if operation == "TokenTransferFromMulti":
        exchangeId = args[0]
        orders = args[1]
        return TokenTransferFromMulti(exchangeId, orders)

def AddToken(symbol, hash):
    """
    :param symbol:token symbol, like "ONT", "ONG"
    :param hash: token script hash,such as ONT,ONG or other token hash, if success, this token can be exchanged on the exchange.
    :return:True or False
    """
    require(CheckWitness(Admin), "not admin")
    require(validateAddress(hash), "invalid contract hash")

    if Get(ctx, concatKey(TOKEN_SYMBOL_PREFIX, symbol)):
        return False
    if Get(ctx, concatKey(TOKEN_HASH_PREFIX, hash)):
        return False



    supportToken = Get(ctx, SUPPORTED_TOKEN)

    if not supportToken:
        tokenMap = {
            symbol: hash
        }
    else:
        tokenMap = Deserialize(supportToken)
        tokenMap[symbol] = hash

    Put(ctx, concatKey(TOKEN_SYMBOL_PREFIX, symbol), symbol)
    Put(ctx, concatKey(TOKEN_HASH_PREFIX, hash), hash)
    Put(ctx, SUPPORTED_TOKEN, Serialize(tokenMap))

    return True

def RemoveToken(symbol, hash):
    """

    :param symbol:token symbol, like "ONT", "ONG"
    :param hash: this token will be removed from the exchange.
    :return:True or False
    """
    require(CheckWitness(Admin), "not admin")

    supportToken = Get(ctx, SUPPORTED_TOKEN)
    if not supportToken:
        return False

    tokenMap = Deserialize(supportToken)

    if tokenMap[symbol] != hash:
        return False

    tokenMap.remove(symbol)
    Put(ctx, SUPPORTED_TOKEN, Serialize(tokenMap))
    Delete(ctx, concatKey(TOKEN_SYMBOL_PREFIX, symbol))
    Delete(ctx, concatKey(TOKEN_HASH_PREFIX, hash))

    return True

def GetTokens():
    """

    :return:Get all the tokens that can be traded in the exchange, it will response a map data structure.
    """
    return Get(ctx, SUPPORTED_TOKEN)

def RegisterExchange(exchangeName, exchangeId):
    """

    :param exchangeName:exchange name, like "Huobi"
    :param exchangeId:exchange Id, essentially it is also a wallet address, only this exchange account can invoke token proxy smart contract
    :return:True or False
    """
    require(CheckWitness(Admin), "not admin")
    require(validateAddress(exchangeId), "invalid exchange Id")
    require(exchangeName != "", "invalid exchange name")

    if Get(ctx, concatKey(EXCHANGE_NAME_PREFIX, exchangeName)):
        return False
    if Get(ctx, concatKey(EXCHANGE_ID_PREFIX, exchangeId)):
        return False

    registerExchange = Get(ctx, REGISTERED_EXCHANGE)

    if not registerExchange:
        exchangeMap = {
            exchangeName: exchangeId
        }
    else:
        exchangeMap = Deserialize(registerExchange)
        exchangeMap[exchangeName] = exchangeId

    Put(ctx, concatKey(EXCHANGE_NAME_PREFIX, exchangeName), exchangeName)
    Put(ctx, concatKey(EXCHANGE_ID_PREFIX, exchangeId), exchangeId)
    Put(ctx, REGISTERED_EXCHANGE, Serialize(exchangeMap))

def RemoveExchange(exchangeName, exchangeId):
    """

    :param exchangeName:exchange name, like "Huobi"
    :param exchangeId:exchange Id
    :return:True or False, if success, the exchange can't invoke token proxy smart contract.
    """
    require(CheckWitness(Admin), "not admin")

    registerExchange = Get(ctx, REGISTERED_EXCHANGE)
    if not registerExchange:
        return False

    exchangeMap = Deserialize(registerExchange)

    if exchangeMap[exchangeName] != exchangeId:
        return False

    exchangeMap.remove(exchangeName)
    Put(ctx, REGISTERED_EXCHANGE, Serialize(exchangeMap))
    Delete(ctx, concatKey(EXCHANGE_NAME_PREFIX, exchangeName))
    Delete(ctx, concatKey(EXCHANGE_ID_PREFIX, exchangeId))

    return True


def GetAuthorizedExchange():
    """

    :return:Get all the exchange list that can invoke token proxy smart contract.
    """
    return Get(ctx, REGISTERED_EXCHANGE)

def TokenTransferFrom(exchangeId, order):
    """

    :param exchangeId:exchange id, Invoked only by registered exchange
    :param order: the order is a map structure.
    :return:True or false, if success, the maker and taker will get purpose token.
    """
    expireTime = order['expireTime']
    require(GetTime() <= expireTime, "order expired")
    require(CheckWitness(exchangeId), "invalid exchange")

    if not Get(ctx, concatKey(EXCHANGE_ID_PREFIX, exchangeId)):
        return False

    maker = order['makerAddress']
    makerAmount = order['makerAssetAmount']
    makerHash = order['makerTokenHash']
    taker = order['takerAddress']
    takerAmount = order['takerAssetAmount']
    takerHash = order['takerTokenHash']
    makerFee = order['makerFee']
    takerFee = order['takerFee']
    feeTokenHash = order['feeTokenHash']
    feeFeceiver = order['feeReceiver']

    if isNativeAsset(makerHash):
        require(transferFromNative(makerHash, ContractAddress, maker, taker, makerAmount), "transfer from maker asset failed")
    else:
        require(DynamicAppCall(bytearray_reverse(makerHash), "transferFrom", [ContractAddress, maker, taker, makerAmount]), "transfer maker token to taker failed")

    Notify("111")

    if isNativeAsset(takerHash):
        require(transferFromNative(takerHash, ContractAddress, taker, maker, takerAmount), "transfer from taker asset failed")
    else:
        require(DynamicAppCall(bytearray_reverse(takerHash), "transferFrom", [ContractAddress, taker, maker, takerAmount]), "transfer taker token to maker failed")

    Notify("222")

    if isNativeAsset(feeTokenHash):
        require(transferFromNative(feeTokenHash, ContractAddress, maker, feeFeceiver, makerFee), "charge maker fee failed")
        require(transferFromNative(feeTokenHash, ContractAddress, taker, feeFeceiver, takerFee), "charge taker fee failed")
    else:
        require(DynamicAppCall(bytearray_reverse(feeTokenHash), "transferFrom", [ContractAddress, maker, feeFeceiver, makerFee]), "charge maker fee failed")
        require(DynamicAppCall(bytearray_reverse(feeTokenHash), "transferFrom", [ContractAddress, taker, feeFeceiver, takerFee]), "charge taker fee failed")

    Notify("success")

    return True

def TokenTransferFromMulti(exchangeId, orders):
    """

    :param exchangeId:exchange id, Invoked only by registered exchange
    :param orders: orders is "TokenTransferFromMulti" fucntion parameter order array list.
    :return:
    """
    require(CheckWitness(exchangeId), "invalid exchange")
    if not Get(ctx, concatKey(EXCHANGE_ID_PREFIX, exchangeId)):
        return False

    for order in orders:
        if len(order) != 1:
            raise Exception("TokenTransferFromMulti params error.")
        if TokenTransferFrom(exchangeId, order) == False:
            raise Exception("TokenTransferFrom failed.")
    return True

def concatKey(str1, str2):
    """
    connect str1 and str2 together as a key
    :param str1: string1
    :param str2:  string2
    :return: string1_string2
    """
    return concat(concat(str1, '_'), str2)

def require(condition, msg):
    if not condition:
        raise Exception(msg)
    return True

def transferONG(fromAcct, toAcct, amount):
    """
    transfer ONG
    :param fromacct:
    :param toacct:
    :param amount:
    :return:
    """
    param = state(fromAcct, toAcct, amount)
    res = Invoke(0, ONGAddress, 'transfer', [param])
    if res and res == b'\x01':
        return True
    else:
        return False

def transferFromNative(contractAddress, spender, fromAcct, toAcct, amount):
    """
    transferFrom ONT/ONG
    :param spender:
    :param fromacct:
    :param toacct:
    :param amount:
    :return:
    """
    param = state(spender, fromAcct, toAcct, amount)
    res = Invoke(0, contractAddress, 'transferFrom', param)
    if res and res == b'\x01':
        return True
    else:
        return False

def validateAddress(address):
    if len(address) != 20:
        return False

    return True

def isNativeAsset(address):
    if address == ONTAddress or address == ONGAddress:
        return True

    return False
