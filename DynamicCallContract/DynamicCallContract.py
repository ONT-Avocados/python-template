from boa.interop.System.App import RegisterAppCall, DynamicAppCall
from boa.interop.System.Runtime import Log, Notify


CallContract = RegisterAppCall('b16e976491982ddccd195dd73bd952a423a5e833', 'operation', 'args')

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

    if operation == "name":
        return getName()
    return False

def DynamicCallContract(revesedContractAddress, operation, params):
    Notify(["bytearray: ", revesedContractAddress])
    res = DynamicAppCall(revesedContractAddress, operation, params)
    Notify(["111_DynamicCall", revesedContractAddress, operation, params])
    Notify(["222_DynamicCall", res])
    return res

def StaticCallContract(opt, params):
    return CallContract(opt, params)



def getName():
    return NAME