```listAndMapSample.py``` has the script hash of ```f8868fb3dca112511494da07bc18d51711094e55```.


```ontology contract invoke --address=f8868fb3dca112511494da07bc18d51711094e55 --params=string:init,[int:0] --gaslimit=200000 --gasprice=500```

coresponds with

```angular2html
{
   "TxHash": "0d528f9c6283213ad992eb290a3681942da6eab66504385d8eda1d3aa8fc4328",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "696e6974206c69737420697320", //init list is
            [
               "01",
               "02",
               "03"
            ]
         ]
      },
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "696e6974206d617020697320", // init map is
            "01",
            "02"
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

```ontology contract invoke --address=f8868fb3dca112511494da07bc18d51711094e55 --params=string:addList,[[int:0,int:10,int:100,int:1000]] --gaslimit=200000 --gasprice=500```

coresponds with

```angular2html
{
   "TxHash": "1885fb9f5403574b5edb0b1e6066593e555d2a6aa30f0bb64f71c65d729bc5e0",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "6265666f7265206164642c206c69737420697320", //before add, list is
            [
               "01",
               "02",
               "03"
            ]
         ]
      },
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "6166746572206164642c206c69737420697320", //after add, list is
            [
               "01",
               "02",
               "03",
               "00",
               "0a",
               "64",
               "e803"
            ]
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
```ontology contract invoke --address=f8868fb3dca112511494da07bc18d51711094e55 --params=string:addMap,[string:key3,int:99] --gaslimit=200000 --gasprice=500```

coresponds with

```angular2html
{
   "TxHash": "31ed89da653f50d7f8d10a53b2673b00d52ccb33d20fcf66150e5d0a451ca8f7",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "6265666f7265206164642c206d617020697320", //before add, map is
            "01",
            "02"
         ]
      },
      {
         "ContractAddress": "f8868fb3dca112511494da07bc18d51711094e55",
         "States": [
            "6166746572206164642c206d617020697320", //after add, map is
            "02",
            "63" //99
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