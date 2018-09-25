from boa.interop.Ontology.Contract import Migrate
from boa.interop.Ontology.Contract import Destroy
from boa.interop.System.Runtime import Notify


def Main(operation, args):
    if operation == "DestroyContract":
        return DestroyContract()
    if operation == "MigrateContract":
        if args[0] != 0:
            Notify("param error")
            return False
        return MigrateContract(args[0])


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
    Migrate(code, "", "", "", "", "", "", "", "")
    Notify(["Migrate successfully"])
    return True