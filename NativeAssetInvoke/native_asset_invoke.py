from boa.interop.Ontology.Native import Invoke
from boa.builtins import ToScriptHash, state
from boa.interop.System.Runtime import Notify


# ONT Big endian Script Hash: 0x0100000000000000000000000000000000000000
OntContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
# ONG Big endian Script Hash: 0x0200000000000000000000000000000000000000
OngContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")


def Main(operation, args):
    if operation == "transferOntOng":
        if len(args) != 4:
            Notify("wrong params")
            return
        return TransferOntOng(args[0], args[1], args[2], args[3])


def TransferOntOng(from_acct, to_acct, ontAmount, ongAmount):
    param = state(from_acct, to_acct, ontAmount)
    res = Invoke(0, OntContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ont error.")
    param = state(from_acct, to_acct, ongAmount)
    Notify("transferONT succeed")
    res = Invoke(0, OngContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ong error.")
    Notify("transferONG succeed")
    return True