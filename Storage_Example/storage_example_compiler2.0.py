OntCversion = '2.0.0'

from ontology.interop.System.Storage import Put, GetContext, Get, Delete
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