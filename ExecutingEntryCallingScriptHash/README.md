The usage api can be found [here](https://apidoc.ont.io/smartcontract/#executionengine-entryscripthash).

ContractB script hash: 4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a

ContractA script hash: b0339f7bea0b2a38ab7294bd41106d354a6b489a


When we invoke ```invokeA``` method within contractA.py through Cli using
```ontology contract invoke --address=b0339f7bea0b2a38ab7294bd41106d354a6b489a --params=string:invokeA,[string:invokeB,[int:999]] --gaslimit=200000 --gasprice=500```,
we get

```
{
   "TxHash": "b8268ff89abcf9e39f531a9c7ce569aaab226eb21dc41f1e1b851d1fe600234d",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a",
         "States": [
            "3131315f696e766f6b6542", //111_invokeB
            "e703" //999
         ]
      },
      {
         "ContractAddress": "4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a",
         "States": [
            "9a486b4a356d1041bd9472ab382a0bea7b9f33b0",
            "0054bb8e669a8314b46dcd5d3144e0ed631004a9",
            "9a9bb5a8a3c19cefc12f45c311f8cad2dad1994d"
         ]
      },
      {
         "ContractAddress": "b0339f7bea0b2a38ab7294bd41106d354a6b489a",
         "States": [
            "3131315f696e766f6b6541", // 111_invokeA
            "0054bb8e669a8314b46dcd5d3144e0ed631004a9",
            "0054bb8e669a8314b46dcd5d3144e0ed631004a9",
            "9a486b4a356d1041bd9472ab382a0bea7b9f33b0"
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

When we invoke ```invokeA``` method within contractA.py through Cli using
```ontology contract invoke --address=b0339f7bea0b2a38ab7294bd41106d354a6b489a --params=string:invokeA,[string:avoidToBeInvokedByContract,[int:0]] --gaslimit=200000 --gasprice=500```,

we get

```
{
   "TxHash": "6d963d17ac3a2f4ffacbd333306529f1c86cfa1d6c6e924a11b46e2035e7c483",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "4d99d1dad2caf811c3452fc1ef9cc1a3a8b59b9a",
         "States": [
            "596f7520617265206e6f7420616c6c6f77656420746f20696e766f6b652074686973206d6574686f64207468726f75676820636f6e7472616374" 
            //You are not allowed to invoke this method through contract
         ]
      },
      {
         "ContractAddress": "b0339f7bea0b2a38ab7294bd41106d354a6b489a",
         "States": [
            "3131315f696e766f6b6541", // 111_invokeA
            "c12ab6712d524d8bd21c895158737a9f8f0422e6",
            "c12ab6712d524d8bd21c895158737a9f8f0422e6",
            "9a486b4a356d1041bd9472ab382a0bea7b9f33b0"
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



When we invoke ```checkHash``` method within contractA.pythrough Cli using
```ontology contract invoke --address=b0339f7bea0b2a38ab7294bd41106d354a6b489a --params=string:checkHash,[int:0] --gaslimit=200000 --gasprice=500```,
we get


```
{
   "TxHash": "007ab582e85642a73687e9618a6148da9c38b54f03e76b094ed23917e7a86791",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "b0339f7bea0b2a38ab7294bd41106d354a6b489a",
         "States": [
            "3131315f636865636b48617368" //111_checkHash
         ]
      },
      {
         "ContractAddress": "b0339f7bea0b2a38ab7294bd41106d354a6b489a",
         "States": [
            "796e304a6d5c6b195e553b36284ed519997d8bed",
            "796e304a6d5c6b195e553b36284ed519997d8bed",
            "9a486b4a356d1041bd9472ab382a0bea7b9f33b0"
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


