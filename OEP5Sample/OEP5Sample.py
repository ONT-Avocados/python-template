"""
A sample of OEP5 smart contract
"""
from boa.interop.System.Storage import GetContext, Get, Put, Delete
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash
from boa.builtins import ToScriptHash, sha256, concat


from boa.interop.System.Runtime import Serialize, Deserialize




# modify to the admin address
admin = ToScriptHash('AQf4Mzu1YJrhz9f3aRkkwSm9n3qhXGSh4p')

NAME = 'My Non-Fungibles Token'
SYMBOL = 'MNFT'


OWNER_BALANCE_PREFIX = 'Balance'
OWNER_OF_TOKEN_PREFIX = 'OwnerOf'
APPROVE_PREFIX = 'Approve'
TOKEN_ID_PREFIX = 'TokenID'
# TOKEN_INDEX_PREFIX, INITED, and TOTAL_SUPPLY for testing usage only
TOKEN_INDEX_PREFIX = 'Index'
TOTAL_SUPPLY = 'TotalSupply'
INITED = 'Initialized'


ctx = GetContext()
selfAddr = GetExecutingScriptHash()

def Main(operation, args):
    if operation == 'name':
        return name()
    if operation == 'symbol':
        return symbol()
    if operation == 'balanceOf':
        if len(args) != 1:
            return False
        owner = args[0]
        return balanceOf(owner)
    if operation == 'ownerOf':
        if len(args) != 1:
            return False
        tokenID = args[0]
        return ownerOf(tokenID)
    if operation == 'transfer':
        if len(args) != 2:
            return False
        toAcct = args[0]
        tokenID = args[1]
        return transfer(toAcct, tokenID)
    if operation == 'transferMulti':
        return transferMulti(args)
    if operation == 'approve':
        if len(args) != 2:
            return False
        toAcct = args[0]
        tokenID = args[1]
        return approve(toAcct, tokenID)
    if operation == 'takeOwnership':
        if len(args) != 2:
            return False
        toAcct = args[0]
        tokenID = args[1]
        return takeOwnership(toAcct, tokenID)

    ############ For testing usage only starts ############
    if operation == 'init':
        return init()
    if operation == 'queryTokenByID':
        if len(args) != 1:
            return False
        tokenID = args[0]
        return queryTokenByID(tokenID)
    if operation == 'totalSupply':
        return totalSupply()
    if operation == "getApproved":
        if len(args) != 1:
            return False
        tokenID = args[0]
        return getApproved(tokenID)
    if operation == "queryTokenIDByIndex":
        if len(args) != 1:
            return False
        index = args[0]
        return queryTokenIDByIndex(index)
    ############ For testing usage only ends ############
    return False


def name():
    """
    :return: name of the token
    """
    return NAME


def symbol():
    """
    :return: symbol of the token
    """
    return SYMBOL


def balanceOf(owner):
    """
    :param owner:
    :return: token balance of the owner
    """
    if len(owner) != 20:
        return False
    key = concatkey(OWNER_BALANCE_PREFIX, owner)
    return Get(ctx, key)


def ownerOf(tokenID):
    """
    get the owner of the unique token with this tokenID
    :param tokenID: the tokenID should be unique and exist.
    :return: the owner address of the token with this unique tokenID
    """
    key = concatkey(OWNER_OF_TOKEN_PREFIX, tokenID)
    owner = Get(ctx, key)
    if not owner:
        raise Exception('ownerOf failed!')
    return owner


def transfer(toAcct, tokenID):
    """
    transfer the token with tokenID to the toAcct
    :param toAcct: to account address
    :param tokenID: the unique token's ID, type should be ByteArray
    :return: False means failure, True means success.
    """
    tokenOwner = ownerOf(tokenID)
    if CheckWitness(tokenOwner) == False:
        return False
    if len(toAcct) != 20:
        raise Exception('address length error!')

    ownerKey = concatkey(OWNER_OF_TOKEN_PREFIX, tokenID)
    fromAcct = Get(ctx, ownerKey)
    balanceKey = concatkey(OWNER_BALANCE_PREFIX, fromAcct)
    fromBalance = Get(ctx, balanceKey)
    if fromBalance >= 1:
        # decrease fromAccount token balance
        Put(ctx, balanceKey, fromBalance - 1)
    else:
        raise Exception('fromBalance error')
    # set the owner of tokenID to toAcct
    Put(ctx, ownerKey, toAcct)
    # increase toAccount token balance
    balanceKey = concatkey(OWNER_BALANCE_PREFIX, toAcct)
    Put(ctx, balanceKey, balanceOf(toAcct) + 1)
    
    Delete(ctx, concatkey(APPROVE_PREFIX, tokenID))
    Notify(['transfer', fromAcct, toAcct, tokenID])

    return True


def transferMulti(args):
    '''
    multi transfer
    :param args:[[toAccount1, tokenID1],[toAccount2, tokenID2]]
    :return: True or raise exception
    '''
    for p in args:
        if len(p) != 2:
            raise Exception('transferMulti failed - input error!')
        if transfer(p[0], p[1]) == False:
            raise Exception('transferMulti failed - transfer error!')
    return True


def approve(toAcct, tokenID):
    '''
    approve the token to toAcct address, it can overwrite older approved address
    :param toAcct:
    :param tokenID:
    :return:
    '''
    tokenOwner = ownerOf(tokenID)
    if CheckWitness(tokenOwner) == False:
        return False
    if len(toAcct) != 20:
        raise Exception('address length error!')

    Put(GetContext(), concatkey(APPROVE_PREFIX, tokenID), toAcct)
    Notify(['approval', tokenOwner, toAcct, tokenID])
    return True


def takeOwnership(toAcct, tokenID):
    """
    transfer the approved tokenId token to toAcct
    the invoker can be the owner or the approved account
    toAcct can be any address
    :param toAcct: the account that will be assigned as the new owner of tokenId
    :param tokenID: the tokenId token will be assigned to toAcct
    :return: False or True
    """
    if len(toAcct) != 20:
        raise Exception("toAcct illegal!")
    tokenOwner = ownerOf(tokenID)

    if not tokenOwner:
        return False
    approveKey = concatkey(APPROVE_PREFIX, tokenID)
    approvedAcct = Get(ctx, approveKey)

    if CheckWitness(tokenOwner) != True and CheckWitness(approvedAcct) != True:
        return False

    Delete(ctx, approveKey)
    ownerKey = concatkey(OWNER_OF_TOKEN_PREFIX, tokenID)
    Put(ctx, ownerKey, toAcct)

    fromBalance = balanceOf(tokenOwner)
    toBalance = balanceOf(toAcct)
    # to avoid overflow
    if fromBalance >= 1 and toBalance < toBalance + 1:
        Put(ctx, concatkey(OWNER_BALANCE_PREFIX, tokenOwner), fromBalance - 1)
        Put(ctx, concatkey(OWNER_BALANCE_PREFIX, toAcct), toBalance + 1)

    Notify(['transfer', tokenOwner, toAcct, tokenID])

    return True


def concatkey(str1, str2):
    return concat(concat(str1, '_'), str2)

#################### For testing usage only starts ######################

def init():
    '''
    based on your requirements, initialize the tokens
    :return:
    '''
    # Notify(["111_init"])
    if not Get(ctx, INITED) and CheckWitness(admin) == True:
        Put(ctx, INITED, 'TRUE')
        Put(ctx, TOTAL_SUPPLY, 0)
        tt = createMultiTokens()
        if tt == True:
            # adminBalance = Get(ctx, concatkey(OWNER_BALANCE_PREFIX, admin))
            # Put(ctx, TOTAL_SUPPLY, adminBalance)
            # Notify(["222_init", adminBalance])
            return True
        return False
    else:
        Notify(["222_init"])

    return False


def totalSupply():
    return Get(ctx, TOTAL_SUPPLY)


def queryTokenIDByIndex(idx):
    '''
    query tokenid by index
    :param idx:
    :return:
    '''
    tokenID = Get(ctx, concatkey(TOKEN_INDEX_PREFIX, idx))
    # Notify(["111_queryTokenIDByIndex", tokenID])
    return tokenID


def queryTokenByID(tokenID):
    '''
    query token detail by tokenID
    :param tokenID:
    :return:
    '''
    Notify(["111_queryTokenByID",  tokenID, concatkey(TOKEN_ID_PREFIX, tokenID)])
    token = Get(ctx, concatkey(TOKEN_ID_PREFIX, tokenID))
    token_info = Deserialize(token)
    id = token_info['ID']
    name = token_info['Name']
    image = token_info['Image']
    type = token_info['Type']
    # Notify(["111_token info: ", id, name, image, type])
    return [id, name, image, type]


def getApproved(tokenID):
    '''
    get the approved address of the token
    :param tokenID:
    :return:
    '''
    key = concatkey(APPROVE_PREFIX, tokenID)
    return Get(ctx, key)


def createMultiTokens():
    # Notify(["111_createMultiTokens begins"])

    a1 = {'Name': 'HEART A', 'Image': 'http://images.com/hearta.jpg'}
    a2 = {'Name': 'HEART 2', 'Image': 'http://images.com/heart2.jpg'}
    a3 = {'Name': 'HEART 3', 'Image': 'http://images.com/heart3.jpg'}
    a4 = {'Name': 'HEART 4', 'Image': 'http://images.com/heart4.jpg'}
    a5 = {'Name': 'HEART 5', 'Image': 'http://images.com/heart5.jpg'}
    a6 = {'Name': 'HEART 6', 'Image': 'http://images.com/heart6.jpg'}
    a7 = {'Name': 'HEART 7', 'Image': 'http://images.com/heart7.jpg'}
    a8 = {'Name': 'HEART 8', 'Image': 'http://images.com/heart8.jpg'}
    a9 = {'Name': 'HEART 9', 'Image': 'http://images.com/heart9.jpg'}
    a10 = {'Name': 'HEART 10', 'Image': 'http://images.com/heart10.jpg'}
    a11 = {'Name': 'HEART J', 'Image': 'http://images.com/heartj.jpg'}
    a12 = {'Name': 'HEART Q', 'Image': 'http://images.com/heartq.jpg'}
    a13 = {'Name': 'HEART K', 'Image': 'http://images.com/heartk.jpg'}

    cards = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13]
    for card in cards:
        if createOneToken(card['Name'], card['Image'], 'CARD') != True:
            raise Exception('_createMultiToken failed')
    # Notify(["222_createMultiTokens ends"])
    return True


def createOneToken(name, url, type):
    '''
    create a new token
    :param name:
    :param url:
    :param type:
    :return:
    '''
    # Notify(["111_createOneToken begins"])
    # generate tokenID
    timestamp = GetTime()
    totalSupply = Get(ctx, TOTAL_SUPPLY)
    newTotalSupply = totalSupply + 1
    Put(ctx, TOTAL_SUPPLY, newTotalSupply)
    tmp = concatkey(concatkey(selfAddr, timestamp), newTotalSupply)
    tokenID = sha256(tmp)
    # construct token map
    token = {'ID': tokenID, 'Name': name, 'Image': url, 'Type': type}
    Notify(["111_createOneToken", newTotalSupply, tokenID, concatkey(TOKEN_ID_PREFIX, tokenID)])
    Put(ctx, concatkey(TOKEN_INDEX_PREFIX, newTotalSupply), tokenID)
    ownerKey = concatkey(OWNER_OF_TOKEN_PREFIX, tokenID)
    Put(ctx, ownerKey, admin)
    Put(ctx, concatkey(TOKEN_ID_PREFIX, tokenID), Serialize(token))
    # add to adminBalance
    adminBalance = Get(ctx, concatkey(OWNER_BALANCE_PREFIX, admin))
    Put(ctx, concatkey(OWNER_BALANCE_PREFIX, admin), adminBalance + 1)
    # Notify(["333_createOneToken ends"])
    return True
#################### For testing usage only ends ######################
