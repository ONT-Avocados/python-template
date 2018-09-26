from boa.interop.System.App import RegisterAppCall
from boa.interop.System.Runtime import Log


# Here "749a701ae89c0dbdab9b4b660ba84ee478004219" should your OPE4 contract hash, pls note it's not reversed version
OEP4Contract = RegisterAppCall('749a701ae89c0dbdab9b4b660ba84ee478004219', 'operation', 'args')


def Main(operation, args):
    if operation == "transfer":
        if len(args) != 3:
            Log("len(args)!=3 ")
            return False
        return CallNep5Contract("transfer", args)
    # Here you can define the method name "Name" to anything you want
    if operation == "Name":
        # This "name" below should be consistent with your OEP4Contract methods
        return OEP4Contract("name", 0)
    # Here you can define the method name "BalanceOf" to anything you want
    if operation == "BalanceOf":
        # This "balanceOf" below should be consistent with your OEP4Contract methods
        return OEP4Contract("balanceOf", args)

def CallNep5Contract(operation, params):
    return OEP4Contract(operation, params)

