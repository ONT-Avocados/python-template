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


def Main(operation, args):
    if operation == "transferOntOng":
        if len(args) != 4:
            Notify("wrong params")
            return
        return transferOntOng(args[0], args[1], args[2], args[3])
    if operation == "transferOngToContract":
        return transferOngToContract(args[0], args[1])
    if operation == "balanceOf1":
        return balanceOf1(args[0])
    if operation == "balanceOf2":
        return balanceOf2()

    return False

def transferOntOng(from_acct, to_acct, ont, ong):
    param = state(from_acct, to_acct, ont)
    res = Invoke(0, OntContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ont error.")
    param = state(from_acct, to_acct, ong)
    Notify("transferONT succeed")
    res = Invoke(0, OngContract, "transfer", [param])

    if res and res == b'\x01':
        Notify('transfer succeed')
        return True
    else:
        Notify('transfer failed')

        return False


def transferOngToContract(account, ongAmount):
    selfContractAddress = GetExecutingScriptHash()
    Notify(["111_transferOngToContract", selfContractAddress])
    param = state(account, selfContractAddress, ongAmount)
    ongContractAddress = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
    res = Invoke(0, ongContractAddress, 'transfer', [param])
    if res and res == b'\x01':
        Notify('transfer succeed')
        return True
    else:
        Notify('transfer failed')

        return False

def balanceOf1(acct):
    """
    transfer ONG from contract
    :param acct:
    :return:
    """
    # return ongContract("balanceOf", [acct])
    # return True

    # ONT native contract address
    # contractAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02')
    contractAddress = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
    param = state(acct)
    res = Invoke(0, contractAddress, 'balanceOf', acct)
    return res


def balanceOf2():
    """
    transfer ONG from contract
    :param acct:
    :return:
    """
    # return ongContract("balanceOf", [acct])
    # return True

    # ONT native contract address
    # contractAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02')
    ongContractAddress = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
    param = state(GetExecutingScriptHash())
    res = Invoke(0, ongContractAddress, 'balanceOf', param)

    # res = ONGContract("balanceOf", [acct])

    return res