In ```avoidContractCallAttack``` method, ```callerHash != entryHash``` can prevent this 
method being called by another contract, which can obtain the value of ```randomNumber = getRandomNumber()```.
Therefore, it can effectively avoid contract call attack.

```avoidContractCallAttack.py``` is the target contract with script hash ```3bc5276e6b59444035e577a07f9991011ba38bf7```.
```attackContract.py``` is the attack contract with script hash ```07d6fe13a84a37a8e8c55a01ef46f54a671f6340```.

If we do not use ```if callerHash != entryHash:```, then ```attack``` method in ```attackContract.py```
 will result in the attackContract winning the big prize.
However, if we implement ```if callerHash != entryHash:```, the contract calling attack is avoidable.



Through Cli, when we invoke attackContract using ```ontology contract invoke --address=07d6fe13a84a37a8e8c55a01ef46f54a671f6340 --params=string:attack,[string:cannotAvoidContractCallAttack] --gaslimit=200000 --gasprice=500```,
we will get 
```angular2html
{
   "TxHash": "6accbe2c95116ca448c92f944efac18e6127e2ba919711ed28bd90a21cf014ae",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "3bc5276e6b59444035e577a07f9991011ba38bf7",
         "States": [
            "596f75206861766520776f6e2074686520626967207072697a6521"
            //You have won the big prize!
         ]
      },
      {
         "ContractAddress": "0200000000000000000000000000000000000000",
         "States": [
            "transfer",
            "AQf4Mzu1YJrhz9f3aRkkwSm9n3qhXGSh4p",
            "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",
            10000000
         ]
      }
   ]
}
```



Through Cli, when we invoke attackContract using ```ontology contract invoke --address=07d6fe13a84a37a8e8c55a01ef46f54a671f6340 --params=string:attack,[string:avoidContractCallAttack] --gaslimit=200000 --gasprice=500```,
we will get 
```angular2html
{
   "TxHash": "2fffca6d3cc437c72501f870cc4f1ae5bb342a4ad63e89876a1b6861b5b622e0",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "3bc5276e6b59444035e577a07f9991011ba38bf7",
         "States": [
            "72616e646f6d4e756d6265723a",
            "ae18d005",
            "67756573734e756d6265723a",
            "ae18d005"
         ]
      },
      {
         "ContractAddress": "3bc5276e6b59444035e577a07f9991011ba38bf7",
         "States": [
            "596f7520617265206e6f7420616c6c6f77656420746f20696e766f6b652074686973206d6574686f64207468726f75676820636f6e747261637421"
            //You are not allowed to invoke this method through contract!
         ]
      },
      {
         "ContractAddress": "0200000000000000000000000000000000000000",
         "States": [
            "transfer",
            "AQf4Mzu1YJrhz9f3aRkkwSm9n3qhXGSh4p",
            "AFmseVrdL9f9oyCzZefL9tG6UbviEH9ugK",
            10000000
         ]
      }
   ]
}
```