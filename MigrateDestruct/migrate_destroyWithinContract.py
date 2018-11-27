from boa.interop.Ontology.Contract import Migrate
from boa.interop.Ontology.Contract import Destroy
from boa.interop.System.Runtime import Notify


def Main(operation, args):
    if operation == "DestroyContract":
        return DestroyContract()
    if operation == "MigrateContract":
        if args[0] != 1:
            Notify("param error")
            return False
        return MigrateContract(args[0])
    return False

def DestroyContract():
    Destroy()
    Notify(["Destory"])
    return True

def MigrateContract(code):
    """
    Note that the existing contract will be replaced by the newly migrated contract
    :param code: your avm code
    :return:
    """
    res = Migrate(code, "", "", "", "", "", "")
    if res:
        Notify(["Migrate successfully"])
        return True
    else:
        return False