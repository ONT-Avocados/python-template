from boa.interop.System.Storage import Put, Get, GetContext
from boa.interop.System.Runtime import Notify, Serialize, Deserialize

LISTKEY = "List"
MAPKEY = "Map"

def Main(operation, args):
    if operation == "init":
        return init()
    if operation == "addList":
        elementList = args[0]
        return addList(elementList)
    if operation == "addMap":
        key = args[0]
        value = args[1]
        return addMap(key, value)
    return False

def init():
    # init list
    list1 = [1,2,3]
    list1Info = Serialize(list1)
    Put(GetContext(), LISTKEY, list1Info)
    # init map
    map1 = {
        "key1":1,
        "key2":2
    }
    map1Info = Serialize(map1)
    Put(GetContext(), MAPKEY, map1Info)

    Notify(["init list is ",list1])
    Notify(["init map is ", map1["key1"], map1["key2"]])

    return True

def addList(listToBeAppend):
    list1Info = Get(GetContext(), LISTKEY)
    list1 = Deserialize(list1Info)

    Notify(["before add, list is ", list1])

    for element in listToBeAppend:
        list1.append(element)
    list1Info = Serialize(list1)
    Put(GetContext(), LISTKEY, list1Info)
    Notify(["after add, list is ", list1])

    return list1


def addMap(key, value):
    map1Info = Get(GetContext(), MAPKEY)
    map1 = Deserialize(map1Info)

    Notify(["before add, map is ", map1["key1"], map1["key2"]])

    map1[key] = value
    map1.remove("key1")

    map1Info = Serialize(map1)
    Put(GetContext(), MAPKEY, map1Info)
    Notify(["after add, map is ", map1["key2"], map1[key]])

    return True
