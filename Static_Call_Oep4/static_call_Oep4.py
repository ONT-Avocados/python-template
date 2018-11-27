from boa.interop.System.App import RegisterAppCall
from boa.interop.System.Runtime import Log
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash

# Here "8ef4b22b006b49a85f5a9a4fe4cd42ce1ab809f4" should your OPE4 contract hash, pls note it's not reversed hash
OEP4Contract = RegisterAppCall('8ef4b22b006b49a85f5a9a4fe4cd42ce1ab809f4', 'operation', 'args')

selfContractAddress = GetExecutingScriptHash()

def Main(operation, args):
    
    # Here you can define the method name "checkName" to anything you want
    if operation == "checkName":
        return checkName()
    # Here you can define the method name "checkBalanceOf" to anything you want
    if operation == "checkBalanceOf":
        if len(args) == 1:
            account = args[0]
            return checkBalanceOf(account)
        else:
            return False
    if operation == "checkSelfBalance":
        return checkSelfBalance()
    if operation == "checkTransfer":
        if len(args) != 3:
            Log("len(args)!=3 ")
            return False
        else:
            fromAcct = args[0]
            toAcct = args[1]
            tokenAmount = args[2]
            return checkTransfer(fromAcct, toAcct, tokenAmount)
    if operation == "sendOEP4TokenFromContractTo":
        if len(args) == 2:
            toAcct = args[0]
            tokenAmount = args[1]
            return sendOEP4TokenFromContractTo(toAcct, tokenAmount)
        else:
            return False
    return False


def checkName():
    # This "name" below should be consistent with your OEP4Contract methods
    # return OEP4Contract("name") is wrong
    # return OEP4Contract("name", []) or return OEP4Contract("name", 0) is correct!
    return OEP4Contract("name", 0)
    

def checkBalanceOf(account):
    # This "balanceOf" below should be consistent with your OEP4Contract methods
    # params = account is wrong
    params = [account]
    return OEP4Contract("balanceOf", params)

def checkSelfBalance():
    params = [selfContractAddress]
    return OEP4Contract("balanceOf", params)

def checkTransfer(fromAcct, toAcct, tokenAmount):
    params = [fromAcct, toAcct, tokenAmount]
    return OEP4Contract("transfer", params)

def sendOEP4TokenFromContractTo(toAcct, tokenAmount):
    params = [selfContractAddress, toAcct, tokenAmount]
    return OEP4Contract("transfer", params)
