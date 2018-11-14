from boa.interop.System.ExecutionEngine import GetExecutingScriptHash, GetCallingScriptHash, GetEntryScriptHash
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize



ContractAddress = GetExecutingScriptHash()
def Main(opration, args):
    if opration == "invokeB":
        return invokeB(args[0])
    if opration == "avoidToBeInvokedByContract":
        return avoidToBeInvokedByContract()
    return False


def invokeB(param):
    Notify(["111_invokeB", param])
    # to prevent hack from other contract
    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    Notify([callerHash, entryHash, ContractAddress])
    return True

def avoidToBeInvokedByContract():
    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    if callerHash != entryHash:
        Notify(["You are not allowed to invoke this method through contract"])
        return False
    else:
        Notify(["You can implement what you need to do here!"])
        return True