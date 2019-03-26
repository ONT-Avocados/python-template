OntCversion = '2.0.0'
from ontology.interop.System.App import RegisterAppCall, DynamicAppCall
from ontology.interop.System.Runtime import Log, Notify
from ontology.interop.System.ExecutionEngine import GetExecutingScriptHash

CallContract = RegisterAppCall('ebe0ff4ee0524c2dabcd1331c3c842896bf40b97', 'operation', 'args')
selfContractAddr_ = GetExecutingScriptHash()

# input = b'\x33...\xb1''
# b16e976491982ddccd195dd73bd952a423a5e833

NAME = "Dynamic"

def Main(operation, args):
    if operation == "DynamicCallContract":
        if len(args) != 3:
            return False
        revesedContractAddress = args[0]
        opt = args[1]
        params = args[2]
        return DynamicCallContract(revesedContractAddress, opt, params)
    if operation == "StaticCallContract":
        opt = args[0]
        params = args[1]
        return StaticCallContract(opt,params)

    if operation == "getName":
        return getName()

    if operation == "DynamicSendOng":
        revesedContractAddress = args[0]
        ongAmount = args[1]
        return DynamicSendOng(revesedContractAddress, ongAmount)

    return False


def DynamicCallContract(revesedContractAddress, operation, params):
    Notify(["bytearray: ", revesedContractAddress])
    res = DynamicAppCall(revesedContractAddress, operation, params)
    Notify(["111_DynamicCall", revesedContractAddress, operation, params])
    Notify(["222_DynamicCall", res])
    return res

def DynamicSendOng(revesedContractAddress, ongAmount):
    params = [selfContractAddr_, ongAmount]
    Notify(["params: ", params])
    res = DynamicAppCall(revesedContractAddress, "receiveONG", params)
    Notify(["111_DynamicSendOng", revesedContractAddress, "receiveONG", params])
    Notify(["222_DynamicSendOng", res])
    return res

def StaticCallContract(opt, params):
    return CallContract(opt, params)

def getName():
    return NAME