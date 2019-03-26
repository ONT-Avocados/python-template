OntCversion = '2.0.0'
from ontology.interop.Ontology.Native import Invoke
from ontology.builtins import state
from ontology.interop.System.Runtime import Notify
from ontology.interop.System.ExecutionEngine import GetExecutingScriptHash
from ontology.interop.Ontology.Runtime import Base58ToAddress

# ONT Big endian Script Hash: 0x0100000000000000000000000000000000000000
OntContract = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
# ONG Big endian Script Hash: 0x0200000000000000000000000000000000000000
OngContract = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
# ONTID Big endian Script Hash: 0x0300000000000000000000000000000000000000
OntIDContract = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6Ubvho7BUwN")

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