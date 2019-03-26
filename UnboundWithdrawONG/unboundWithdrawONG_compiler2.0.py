OntOntCversion = '2.0.0'
from ontology.interop.Ontology.Contract import Migrate
from ontology.interop.System.Storage import GetContext, Get, Put, Delete
from ontology.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Deserialize
from ontology.interop.System.ExecutionEngine import GetExecutingScriptHash, GetCallingScriptHash, GetEntryScriptHash
from ontology.interop.Ontology.Native import Invoke
from ontology.interop.Ontology.Runtime import GetCurrentBlockHash
from ontology.builtins import concat, state
from ontology.interop.Ontology.Runtime import Base58ToAddress

ContractAddress = GetExecutingScriptHash()
# ONTAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
# ONGAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02')

ONTAddress = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
ONGAddress = Base58ToAddress("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")


def Main(operation, args):
    if operation == "invest":
        fromAcct = args[0]
        ontAmount = args[1]
        return invest(fromAcct, ontAmount)
    if operation == "withdraw":
        toAcct = args[0]
        ontAmount = args[1]
        return withdraw(toAcct, ontAmount)
    if operation == "checkAllowance":
        account = args[0]
        return checkAllowance(account)
    if operation == "checkWithdraw":
        account = args[0]
        return checkWithdraw(account)
    if operation == "checkBalanceOf":
        ongFlag = args[0]
        account = args[1]
        return checkBalanceOf(ongFlag, account)
    if operation == "unboundOngBalance":
        return unboundOngBalance()
    if operation == "withdrawOng":
        toAcct = args[0]
        return withdrawOng(toAcct)
    return False


def invest(fromAcct, ontAmount):
    transferONT(fromAcct, ContractAddress, ontAmount)
    return True


def withdraw(toAcct, ontAmount):
    transferONT(ContractAddress, toAcct, ontAmount)
    return True


def checkAllowance(account):
    # param = state(ONTAddress, account)
    # if ongFlag == 1:
    #     Notify(["ongFlag", ongFlag])
    #     unboundOngAmount = Invoke(0, ONGAddress, 'allowance', param)
    # else:
    #     Notify(["ongFlag", ongFlag])
    #     unboundOngAmount = Invoke(0, ONTAddress, 'allowance', param)
    # Notify(["checkAllowance", account, unboundOngAmount])

    param = state(ONTAddress, account)
    unboundOngAmount = Invoke(0, ONGAddress, 'allowance', param)
    Notify(["checkAllowance", account, unboundOngAmount])

    return unboundOngAmount


def checkWithdraw(account):
    allowanceOng = checkAllowance(account)
    withdrawOngAmount = allowanceOng / 2
    params = state(account, ONTAddress, account, withdrawOngAmount)
    res = Invoke(0, ONGAddress, 'transferFrom', params)
    if res and res == b'\x01':
        Notify(["withdraw ong successful!"])
        return True
    else:
        Notify(["withdraw ong failed!"])
        return False


def checkBalanceOf(ongFlag, account):
    param = state(ContractAddress)
    # do not use [param]
    res = Invoke(0, ONGAddress, 'balanceOf', param)
    Notify(["ContractAddress", ContractAddress, res])

    param = state(account)
    if ongFlag == 1:
        Notify(["ongFlag", ongFlag])
        res = Invoke(0, ONGAddress, 'balanceOf', param)
    else:
        Notify(["ongFlag", ongFlag])
        res = Invoke(0, ONTAddress, 'balanceOf', param)
    Notify(["checkBalanceOf", account, res])
    return res


def unboundOngBalance():
    return checkAllowance(ContractAddress)


def withdrawOng(toAcct):
    param = state(ONTAddress, ContractAddress)
    unboundOngAmount = Invoke(0, ONGAddress, 'allowance', param)
    Notify(["unboundOngAmount", unboundOngAmount])
    if unboundOngAmount > 0:
        unboundOngAmount = 147
        params = state(ContractAddress, ONTAddress, toAcct, unboundOngAmount)
        res = Invoke(0, ONGAddress, "transferFrom", params)
        if res and res == b'\x01':
            Notify(["withdraw ong successful!"])
            return True
        else:
            Notify(["withdraw ong failed!"])
            return False
    else:
        Notify(["Not enough unboundOngAmount", unboundOngAmount])
        return False


def transferONT(fromAcct, toAcct, ontAmount):
    """
    transfer ONG
    :param fromacct:
    :param toacct:
    :param amount:
    :return:
    """
    param = state(fromAcct, toAcct, ontAmount)
    res = Invoke(0, ONTAddress, 'transfer', [param])
    if res and res == b'\x01':
        Notify(["transfer ONT successful!"])
        return True
    else:
        Notify(["transfer ONT failed!"])
        return False
