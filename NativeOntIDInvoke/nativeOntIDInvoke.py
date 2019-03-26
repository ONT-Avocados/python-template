from boa.interop.Ontology.Native import Invoke
from boa.builtins import ToScriptHash, state
from boa.interop.System.Runtime import Notify
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash

# ONT Big endian Script Hash: 0x0100000000000000000000000000000000000000
OntContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
# ONG Big endian Script Hash: 0x0200000000000000000000000000000000000000
OngContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
# ONTID Big endian Script Hash: 0x0300000000000000000000000000000000000000
OntIDContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6Ubvho7BUwN")

def Main(operation, args):
    if operation == "preInvokeGetDDO":
        if len(args) != 1:
            Notify("wrong params")
            return False
        return preInvokeGetDDO(args[0])
    return False

def preInvokeGetDDO(id):
    param = state(id)
    res = Invoke(0, OntIDContract, "getDDO", param)
    return res