from boa.interop.System.App import RegisterAppCall
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash, GetCallingScriptHash, GetEntryScriptHash
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize


# Here "4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a" should your contract hash, pls note it's not reversed hash
ContractB = RegisterAppCall('4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a', 'operation', 'args')

ContractAddress = GetExecutingScriptHash()


def Main(opration, args):
    if opration == "invokeA":
        opt = args[0]
        params = args[1]
        return invokeA(opt, params)
    if opration == "checkHash":
        return checkHash()
    return False

def invokeA(operation, params):
    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    Notify(["111_invokeA",callerHash, entryHash, ContractAddress])
    return ContractB(operation, params)


def checkHash():
    Notify(["111_checkHash"])
    # to prevent hack from other contract
    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    Notify([callerHash, entryHash, ContractAddress])
    return True
