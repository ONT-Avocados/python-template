from boa.interop.Ontology.Native import Invoke
from boa.builtins import ToScriptHash, state
from boa.interop.System.Runtime import Notify
from boa.interop.System.ExecutionEngine import GetExecutingScriptHash


# ONT Big endian Script Hash: 0x0100000000000000000000000000000000000000
OntContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
# ONG Big endian Script Hash: 0x0200000000000000000000000000000000000000
OngContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")


selfContractAddress = GetExecutingScriptHash()

def Main(operation, args):
    if operation == "transferOntOng":
        if len(args) == 4:
            fromAcct = args[0]
            toAcct = args[1]
            ontAmount = args[2]
            ongAmount = args[3]
            return transferOntOng(fromAcct, toAcct, ontAmount, ongAmount)
        else:
            return False
    if operation == "transferOngToContract":
        if len(args) == 2:
            fromAccount = args[0]
            ongAmount = args[1]
            return transferOngToContract(fromAccount, ongAmount)
        else:
            return False
    if operation == "checkSelfContractONGAmount":
        return checkSelfContractONGAmount()
    return False

def transferOntOng(fromAcct, toAcct, ontAmount, ongAmount):
    param = state(fromAcct, toAcct, ontAmount)
    res = Invoke(0, OntContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ont error.")
    param = state(fromAcct, toAcct, ongAmount)
    Notify("transferONT succeed")
    res = Invoke(0, OngContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ong error.")
    Notify("transferONG succeed")
    return True


def transferOngToContract(fromAccount, ongAmount):
    Notify(["111_transferOngToContract", selfContractAddress])
    param = state(fromAccount, selfContractAddress, ongAmount)
    res = Invoke(0, OngContract, 'transfer', [param])
    if res and res == b'\x01':
        Notify('transfer Ong succeed')
        return True
    else:
        Notify('transfer Ong failed')
        return False


def checkSelfContractONGAmount():
    param = state(selfContractAddress)
    # do not use [param]
    res = Invoke(0, OngContract, 'balanceOf', param)
    return res