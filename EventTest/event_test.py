from boa.interop.System.Action import RegisterAction

Transfer = RegisterAction('transfer_test', 'a', 'b', 'c')
Refund = RegisterAction('refund_test', 'to', 'amount')


def Main(operation, args):
    if operation == "test1":
        return test()
    if operation =="test2":
        return test1()
    return False

def test():
    a = 2
    b = 5
    c = a + b
    Transfer(a, b, c)
    return True

def test1():
    to = 'somebody'
    amount = 52
    Refund(to, amount)
    return True
