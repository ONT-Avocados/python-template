OntCversion = '2.0.0'
from ontology.interop.System.Runtime import Notify
from ontology.interop.System.Storage import Put, Get, GetContext
from ontology.interop.System.ExecutionEngine import GetExecutingScriptHash
from ontology.builtins import concat, state
from ontology.interop.System.Runtime import CheckWitness, Notify, GetTime
from ontology.interop.Ontology.Runtime import Base58ToAddress
from ontology.interop.System.Storage import Get, GetContext, Put, Delete
from ontology.interop.Ontology.Native import Invoke
from ontology.interop.Ontology.Contract import Migrate
TOTAL_SUPPLY = 'totalsupply'
ONGContractAddress_ = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")
selfContractAddr_ = GetExecutingScriptHash()

def Main(operation, args):

    if operation == "check":
        return check()
    if operation == "receiveONG":
        account = args[0]
        ongAmount = args[1]
        return receiveONG(account, ongAmount)
    return False


def check():
    Put(GetContext(), TOTAL_SUPPLY, 10000)
    Notify(["11_check", 10000])
    return Get(GetContext(), TOTAL_SUPPLY)


def receiveONG(account, ongAmount):
    Notify(["111_receiveONG"])
    # Require(_transferONG(account, selfContractAddr_, ongAmount))
    res = _transferONG(account, selfContractAddr_, ongAmount)
    if res == False:
        Notify(["receiveONG failed!"])
        return False
    else:
        Notify(["receiveONG success!"])
        return True


def _transferONG(fromAcct, toAcct, amount):
    """
     transfer amount of ONG from fromAcct to toAcct
     :param fromAcct:
     :param toAcct:
     :param amount:
     :return:
     """
    # if CheckWitness(fromAcct):
    param = state(fromAcct, toAcct, amount)
    res = Invoke(0, ONGContractAddress_, 'transfer', [param])
    if res and res == b'\x01':
        return True
    else:
        return False
    # else:
    #     return False