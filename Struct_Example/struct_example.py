from boa.interop.System.Runtime import Notify, CheckWitness
from boa.interop.Ontology.Native import Invoke
from boa.builtins import state

contractAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')


def Main(operation, args):
    if operation == 'transfer':
        fromacct = args[0]
        toacct = args[1]
        amount = args[2]
        return transferONT(fromacct,toacct,amount)


    return False


def transferONT(fromacct,toacct,amount):
    """
    transfer ONT
    :param fromacct:
    :param toacct:
    :param amount:
    :return:
    """
    if CheckWitness(fromacct):

        param = makeState(fromacct, toacct, amount)
        res = Invoke(1, contractAddress, 'transfer', [param])
        Notify(["11111",res])

        if res and res == b'\x01':
            Notify('transfer succeed')
            return True
        else:
            Notify('transfer failed')

            return False

    else:
        Notify('checkWitness failed')
        return False


def makeState(fromacct,toacct,amount):
    return state(fromacct, toacct, amount)