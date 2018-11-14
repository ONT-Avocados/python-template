from boa.interop.System.ExecutionEngine import GetCallingScriptHash, GetEntryScriptHash
from boa.interop.System.Runtime import Notify
from boa.interop.Ontology.Runtime import GetRandomHash


def Main(opration, args):
    if opration == "avoidContractCallAttack":
        guessNumber = args[0]
        return avoidContractCallAttack(guessNumber)
    if opration == "cannotAvoidContractCallAttack":
        guessNumber = args[0]
        return cannotAvoidContractCallAttack(guessNumber)
    return False

def avoidContractCallAttack(guessNumber):

    randomNumber = getRandomNumber()

    callerHash = GetCallingScriptHash()
    entryHash = GetEntryScriptHash()
    Notify(["randomNumber:", randomNumber, "guessNumber:", guessNumber])
    if callerHash != entryHash:
        Notify(["You are not allowed to invoke this method through contract!"])
        return False
    else:
        Notify(["You can implement what you need to do here!"])
        if guessNumber == randomNumber:
            Notify(["You have won the big prize!"])
        return True

def cannotAvoidContractCallAttack(guessNumber):

    randomNumber = getRandomNumber()

    if guessNumber == randomNumber:
        Notify(["You have won the big prize!"])
    return True


def getRandomNumber():
    randomHash = GetRandomHash()
    randomNumber = abs(randomHash) % 100000000
    return randomNumber