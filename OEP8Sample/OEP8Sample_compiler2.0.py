OntCversion = '2.0.0'
"""
This is a sample of OEP-8 smart contract
"""
from ontology.interop.System.Storage import GetContext, Get, Put, Delete
from ontology.interop.System.Runtime import CheckWitness, Notify
from ontology.interop.System.Action import RegisterAction
from ontology.builtins import concat
from ontology.interop.Ontology.Runtime import Base58ToAddress

"""
https://github.com/ONT-Avocados/python-template/blob/master/libs/Utils.py
"""
def Revert():
    """
    Revert the transaction. The opcodes of this function is `09f7f6f5f4f3f2f1f000f0`,
    but it will be changed to `ffffffffffffffffffffff` since opcode THROW doesn't
    work, so, revert by calling unused opcode.
    """
    raise Exception(0xF1F1F2F2F3F3F4F4)


"""
https://github.com/ONT-Avocados/python-template/blob/master/libs/SafeCheck.py
"""
def Require(condition):
    """
	If condition is not satisfied, return false
	:param condition: required condition
	:return: True or false
	"""
    if not condition:
        Revert()
    return True

def RequireScriptHash(key):
    """
    Checks the bytearray parameter is script hash or not. Script Hash
    length should be equal to 20.
    :param key: bytearray parameter to check script hash format.
    :return: True if script hash or revert the transaction.
    """
    Require(len(key) == 20)
    return True

def RequireWitness(witness):
    """
	Checks the transaction sender is equal to the witness. If not
	satisfying, revert the transaction.
	:param witness: required transaction sender
	:return: True if transaction sender or revert the transaction.
	"""
    Require(CheckWitness(witness))
    return True

"""
https://github.com/ONT-Avocados/python-template/blob/master/libs/SafeMath.py
"""

def Add(a, b):
    """
	Adds two numbers, throws on overflow.
	"""
    c = a + b
    Require(c >= a)
    return c

def Sub(a, b):
    """
    Substracts two numbers, throws on overflow (i.e. if subtrahend is greater than minuend).
    :param a: operand a
    :param b: operand b
    :return: a - b if a - b > 0 or revert the transaction.
    """
    Require(a>=b)
    return a-b

def Mul(a, b):
    """
    Multiplies two numbers, throws on overflow.
    :param a: operand a
    :param b: operand b
    :return: a - b if a - b > 0 or revert the transaction.
    """
    if a == 0:
        return 0
    c = a * b
    Require(c / a == b)
    return c

def Div(a, b):
    """
    Integer division of two numbers, truncating the quotient.
    """
    Require(b > 0)
    c = a / b
    return c


TransferEvent = RegisterAction("transfer", "fromAcct", "toAcct", "tokenId", "amount")
ApprovalEvent = RegisterAction("approval", "owner", "spender", "tokenId", "amount")

# modify to the admin address
admin = Base58ToAddress('XXXX')

# TOKEN_ID1 is used to identify different tokens, to help store the token name, token symbol and balance
TOKEN_ID_LIST = [b'\x01', b'\x02', b'\x03', b'\x04', b'\x05']

# TOKEN_ID + NAME --- to store the name of the TOKEN_ID token
NAME = 'Name'
# TOKEN_ID + SYMBOL --- to store the symbol of the TOKEN_ID token
SYMBOL = 'Symbol'
# TOKEN_ID+ BALANCE + address --- to store the balance of address in terms of the TOKEN_ID token
BALANCE = 'Balance'
# TOKEN_ID + TOTAL_SUPPLY  --- to store the total supply of the TOKEN_ID token
TOTAL_SUPPLY = 'TotalSupply'
# TOKEN_ID + APPROVE + owner + spender -- to store the approved TOKEN_ID amount to the spender by the owner
APPROVE = 'Approve'
# INITED --- to store "TRUE" in order to make sure this contract can only be deployed once
INITED = 'Initialized'


def Main(operation, args):
    if operation == "name":
        if len(args) != 1:
            return False
        tokenId = args[0]
        return name(tokenId)
    if operation == "symbol":
        if len(args) != 1:
            return False
        tokenId = args[0]
        return symbol(tokenId)
    if operation == "totalSupply":
        if len(args) != 1:
            return False
        tokenId = args[0]
        return totalSupply(tokenId)
    if operation == "balanceOf":
        if len(args) != 2:
            return False
        account = args[0]
        tokenId = args[1]
        return balanceOf(account, tokenId)
    if operation == "transfer":
        if len(args) != 4:
            return False
        fromAcct = args[0]
        toAcct = args[1]
        tokenId = args[2]
        amount = args[3]
        return transfer(fromAcct, toAcct, tokenId, amount)
    if operation == "transferMulti":
        return transferMulti(args)
    if operation == "approve":
        if len(args) != 4:
            return False
        owner = args[0]
        spender = args[1]
        tokenId = args[2]
        amount = args[3]
        return approve(owner, spender, tokenId, amount)
    if operation == "approveMulti":
        return approveMulti(args)
    if operation == "allowance":
        if len(args) != 3:
            return False
        owner = args[0]
        spender = args[1]
        tokenId = args[2]
        return allowance(owner, spender, tokenId)
    if operation == "transferFrom":
        if len(args) != 5:
            return False
        spender = args[0]
        fromAcct = args[1]
        toAcct = args[2]
        tokenId = args[3]
        amount = args[4]
        return transferFrom(spender, fromAcct, toAcct, tokenId, amount)
    if operation == "transferFromMulti":
        return transferFromMulti(args)
    ####################### Optional methods begin ########################
    # init() should be invoked first after the contract is deployed
    if operation == "init":
        if len(args) != 0:
            return False
        return init()
    if operation == "balancesOf":
        if len(args) != 1:
            return False
        account = args[0]
        return balancesOf(account)
    if operation == "totalBalanceOf":
        if len(args) != 1:
            return False
        account = args[0]
        return totalBalanceOf(account)
    # only admin can mint token
    if operation == "mint":
        if len(args) != 2:
            return False
        tokenId = args[0]
        tokenAmount = args[1]
        return mint(tokenId, tokenAmount)
    ####################### Optional methods end ########################
    return False


def name(tokenId):
    """
    :param tokenId: helps to format name key = tokenId + NAME
    :return: name of the token with tokenId
    """
    return Get(GetContext(), concatkey(tokenId, NAME))


def symbol(tokenId):
    """
    :param tokenId: helps to format symbol key = tokenId + SYMBOL
    :return: symbol of token with tokenId
    """
    return Get(GetContext(), concatkey(tokenId, SYMBOL))


def totalSupply(tokenId):
    """
    :param tokenId:  helps to format totalSupply key = tokenId + TOTAL_SUPPLY
    :return: total supply of token with tokenId
    """
    return Get(GetContext(), concatkey(tokenId, TOTAL_SUPPLY))


def balanceOf(acct, tokenId):
    """
    get balance of accout in terms of token with the tokenId
    :param acct: used to check the acct balance
    :param tokenId: the tokenId determines which token balance of acct needs to be checked
    :return: the balance of acct in terms of tokenId tokens
    """
    return Get(GetContext(), concatkey(concatkey(tokenId, BALANCE), acct))


def transfer(fromAcct, toAcct, tokenId, amount):
    """
    transfer amount of tokens in terms of tokenId token from fromAcct to the toAcct
    :param fromAcct:
    :param toAcct:
    :param tokenId:
    :param amount:
    :return:
    """
    RequireWitness(fromAcct)
    Require(checkTokenId(tokenId))
    RequireScriptHash(fromAcct)
    RequireScriptHash(toAcct)

    balanceKey = concatkey(tokenId, BALANCE)
    fromKey = concatkey(balanceKey, fromAcct)
    fromBalance = Get(GetContext(), fromKey)
    if amount > fromBalance or amount <= 0:
        return False
    if amount == fromBalance:
        Delete(GetContext(), fromKey)
    else:
        Put(GetContext(), fromKey, Sub(fromBalance, amount))

    toKey = concatkey(balanceKey, toAcct)
    toBalance = Get(GetContext(), toKey)
    Put(GetContext(), toKey, Add(toBalance, amount))

    TransferEvent(fromAcct, toAcct, tokenId, amount)

    return True


def transferMulti(args):
    """
    multi transfer
    :param args:[[fromAccount1, toAccount1, tokenId1, amount1],[fromAccount2, toAccount2, tokenId2, amount2]]
    :return: True or raise exception
    """
    for p in args:
        if len(p) != 4:
            raise Exception('transferMulti failed - input error!')
        if transfer(p[0], p[1], p[2], p[3]) == False:
            raise Exception('transferMulti failed - transfer error!')
    return True


def approve(owner, spender, tokenId, amount):
    """
    approve amount of the tokenId token to toAcct address, it can overwrite older approved amount
    :param owner:
    :param spender:
    :param tokenId:
    :param amount:
    :return:
    """
    res = int(owner)
    RequireWitness(owner)
    RequireScriptHash(owner)
    RequireScriptHash(spender)
    Require(checkTokenId(tokenId))

    ownerBalance = balanceOf(owner, tokenId)
    # you can use "if" to notify the corresponding message, or use Require to raise exception
    Require(ownerBalance >= amount)
    Require(amount > 0)
    key = concatkey(concatkey(concatkey(tokenId, APPROVE), owner), spender)
    Put(GetContext(), key, amount)

    ApprovalEvent(owner, spender, tokenId, amount)

    return True


def approveMulti(args):
    """
    multi approve
    :param args: args:[[owner1, spender1, tokenId1, amount1],[owner2, spender2, tokenId2, amount2]]
    :return:
    """
    for p in args:
        if len(p) != 4:
            raise Exception('approveMulti failed - input error!')
        if approve(p[0], p[1], p[2], p[3]) == False:
            raise Exception('approveMulti failed - approve error!')
    return True


def allowance(owner, spender, tokenId):
    """
    :param owner:
    :param spender:
    :param tokenId:
    :return:
    """
    key = concatkey(concatkey(concatkey(tokenId, APPROVE), owner), spender)
    return Get(GetContext(), key)


def transferFrom(spender, fromAcct, toAcct, tokenId, amount):
    """
    :param tokenId: this tokenId token should be approved by its owner to toAcct
    :param toAcct: spender
    :param amount: False or True
    :return:
    """
    RequireWitness(spender)
    RequireScriptHash(spender)
    RequireScriptHash(fromAcct)
    RequireScriptHash(toAcct)
    Require(checkTokenId(tokenId))

    fromKey = concatkey(concatkey(tokenId, BALANCE), fromAcct)
    fromBalance = Get(GetContext(), fromKey)
    Require(fromBalance >= amount)
    Require(amount > 0)
    toKey = concatkey(concatkey(tokenId, BALANCE), toAcct)


    approvedKey = concatkey(concatkey(concatkey(tokenId, APPROVE), fromAcct), spender)
    approvedAmount = Get(GetContext(), approvedKey)

    if amount > approvedAmount:
        raise Exception('you are not allowed to withdraw too many tokens')
    elif amount == approvedAmount:
        Delete(GetContext(), approvedKey)
        Put(GetContext(), fromKey, Sub(fromBalance, amount))
    else:
        Put(GetContext(), approvedKey, Sub(approvedAmount, amount))
        Put(GetContext(), fromKey, Sub(fromBalance, amount))

    toBalance = Get(GetContext(), toKey)
    Put(GetContext(), toKey, Add(toBalance, amount))

    TransferEvent(fromAcct, toAcct, tokenId, amount)

    return True


def transferFromMulti(args):
    """
    multiple transferFrom
    :param args: args:[[spender1, fromAcct1, toAcct1, tokenId1, amount1],[spender2, fromAcct2, toAcct2, tokenId2, amount2]]
    :return:
    """
    for p in args:
        if len(p) != 5:
            raise Exception('transferFromMulti failed - input error!')
        if transferFrom(p[0], p[1], p[2], p[3], p[4]) == False:
            raise Exception('transferFromMulti failed - transfer error!')
    return True


def concatkey(str1, str2):
    return concat(concat(str1, '_'), str2)


#################### Optional methods defination starts  ######################
def init():
    '''
    based on your requirements, initialize the tokens
    Only admin can init the contract
    :return:
    '''
    RequireWitness(admin)
    if not Get(GetContext(), INITED):
        tt = createMultiTypeToken()
        if tt == True:
            Put(GetContext(), INITED, 'TRUE')
            return True
        raise Exception("init error")

    return False

def mint(tokenId, tokenAmount):
    """
    only admin can mint token
    :param tokenId:
    :param tokenAmount:
    :return:
    """
    Require(CheckWitness(admin))
    Require(checkTokenId(tokenId))
    oldTokenSupply = totalSupply(tokenId)
    Require(tokenAmount > 0)
    newTokenSupply = Add(tokenAmount, oldTokenSupply)

    Put(GetContext(), concatkey(tokenId, TOTAL_SUPPLY), newTokenSupply)


    Put(GetContext(), concatkey(concatkey(tokenId, BALANCE), admin), Add(tokenAmount, balanceOf(admin, tokenId)))
    TransferEvent('', admin, tokenId, tokenAmount)

    return True

def createMultiTypeToken():
    Index = [0, 1, 2, 3, 4]
    tokenNameList = ['TokenNameFirst', 'TokenNameSecond', 'TokenNameThird', 'TokenNameFourth', 'TokenNameFifth']
    tokenSymbolList = ['TNF', 'TNS', 'TNH', 'TNO', 'TNI']
    tokenSupplyList = [100000, 200000, 300000, 400000, 500000]

    for index in Index:
        # get name, symbol, totalsupply
        tokenName = tokenNameList[index]
        tokenSymbol = tokenSymbolList[index]
        tokenTotalSupply = tokenSupplyList[index]

        tokenId = TOKEN_ID_LIST[index]

        # initiate token name
        Put(GetContext(), concatkey(tokenId, NAME), tokenName)
        # initiate token symbol
        Put(GetContext(), concatkey(tokenId, SYMBOL), tokenSymbol)
        # initiate token totalSupply
        Put(GetContext(), concatkey(tokenId, TOTAL_SUPPLY), tokenTotalSupply)
        # transfer all the tokens to admin
        Put(GetContext(), concatkey(concatkey(tokenId, BALANCE), admin), tokenTotalSupply)
        TransferEvent('', admin, tokenId, tokenTotalSupply)

    return True

def totalBalanceOf(account):
    """
    :param account:
    :return: the total balance of 5 type of tokens
    """
    Index = [0, 1, 2, 3, 4]
    totalBalance = 0
    for index in Index:
        tokenId = TOKEN_ID_LIST[index]
        totalBalance = Add(totalBalance, Get(GetContext(), concatkey(concatkey(tokenId, BALANCE), account)))
    return totalBalance


def balancesOf(account):
    """
    :param account:
    :return: the different balances of account
    """
    Index = [0, 1, 2, 3, 4]
    balancesList = []
    for index in Index:
        tokenId = TOKEN_ID_LIST[index]
        balancesList.append(Get(GetContext(), concatkey(concatkey(tokenId, BALANCE), account)))
    return balancesList

def checkTokenId(tokenId):
    # here we check if the tokenId is legal with the help of getting its name
    if Get(GetContext(), concatkey(tokenId, NAME)):
        return True
    else:
        return False
#################### Optional methods defination starts ######################