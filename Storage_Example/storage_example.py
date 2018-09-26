from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, GetContext, Get, Delete
from template_contract_test.libs.SafeMath import *

ctx = GetContext()


def Main(operation, args):
    if operation == "TestStorage":
        return TestStorage()


def TestStorage():
    Put(ctx, "key", 100)
    v = Get(ctx, "key")
    Notify(v)

    Delete(ctx, "key")
    Notify(Get(ctx, "key"))


    Notify(["test", 100])
    a = Sqrt(110)
    Notify(["a", a])
    return a

    # b = Sqrt(101)
    # Notify(["b = ", b])
    # c = Pwr(3,4)
    # Notify(["c = ", c])