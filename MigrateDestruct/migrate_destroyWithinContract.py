from boa.interop.Ontology.Contract import Migrate
from boa.interop.Ontology.Contract import Destroy
from boa.interop.System.Runtime import Notify


def Main(operation, args):
    if operation == "DestroyContract":
        return DestroyContract()
    if operation == "MigrateContract":
        code = args[0]
        return MigrateContract(code)


def DestroyContract():
    Destroy()
    Notify(["Destory"])
    return True

def MigrateContract(code):
    """
    Note that the existing contract will not replaced by the newly migrated contract
    :param code:
    :return:
    """
    Migrate(code, "", "", "", "", "", "", "", "")

    Notify(["Migrate"])
    return True