This contract indicates non-fungible tokens, allows tokens on ONT to be convenient used by other applications.
##### Notes

###### 1. Global Variable

These are only for testing usage, aims to check the contract works properly. You can modify them based on your needs.
```
# TOKEN_INDEX_PREFIX, INITED, and TOTAL_SUPPLY for testing usage only
TOKEN_INDEX_PREFIX = 'Index'
TOTAL_SUPPLY = 'TotalSupply'
INITED = 'Initialized'
```
###### 2. Optional operation in main

In the main function, these operations are defined in order to check the methods within the contract more conveniently.
```angular2html
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
    
    
```

###### 3. Optional operation defination

This part defines some optional methods (operation) for testing convenience. You can write your unique token based on what you need.

```angular2html
#################### For testing usage only starts ######################

def init():
    '''
    based on your requirements, initialize the tokens
    :return:
    '''
    Notify(["111_init"])
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
    Notify(["111_queryTokenIDByIndex", tokenID])
    return


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
    Notify(["111_token info: ", id, name, image, type])
    return True


def getApproved(tokenID):
    '''
    get the approved address of the token
    :param tokenID:
    :return:
    '''
    key = concatkey(APPROVE_PREFIX, tokenID)
    return Get(ctx, key)


def createMultiTokens():
    Notify(["111_createMultiTokens begins"])

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
    Notify(["222_createMultiTokens ends"])
    return True


def createOneToken(name, url, type):
    '''
    create a new token
    :param name:
    :param url:
    :param type:
    :return:
    '''
    Notify(["111_createOneToken begins"])
    # generate tokenID
    timestamp = GetTime()
    totalSupply = Get(ctx, TOTAL_SUPPLY)
    newTotalSupply = totalSupply + 1
    Put(ctx, TOTAL_SUPPLY, newTotalSupply)
    tmp = concatkey(concatkey(selfAddr, timestamp), newTotalSupply)
    tokenID = sha256(tmp)
    # construct token map
    token = {'ID': tokenID, 'Name': name, 'Image': url, 'Type': type}
    Notify(["222_createOneToken", newTotalSupply, tokenID, concatkey(TOKEN_ID_PREFIX, tokenID)])
    Put(ctx, concatkey(TOKEN_INDEX_PREFIX, newTotalSupply), tokenID)
    ownerKey = concatkey(OWNER_OF_TOKEN_PREFIX, tokenID)
    Put(ctx, ownerKey, admin)
    Put(ctx, concatkey(TOKEN_ID_PREFIX, tokenID), Serialize(token))
    # add to adminBalance
    adminBalance = Get(ctx, concatkey(OWNER_BALANCE_PREFIX, admin))
    Put(ctx, concatkey(OWNER_BALANCE_PREFIX, admin), adminBalance + 1)
    Notify(["333_createOneToken ends"])
    return True
#################### For testing usage only ends ######################
```