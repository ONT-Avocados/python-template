from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, Get, GetContext
TOTAL_SUPPLY = 'totalsupply'

def Main(operation, args):

    if operation == "check":
        return check()
    return False

def check():
    Put(GetContext(), TOTAL_SUPPLY, 10000)
    Notify(["11_check", 10000])
    return Get(GetContext(), TOTAL_SUPPLY)
