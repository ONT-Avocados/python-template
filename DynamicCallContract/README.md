```DynamicCallContract.py``` with script hash 2c2e3ab6a13134c6b2cf92e34d458c98332807f6
```CheckContract.py``` with script hash b16e976491982ddccd195dd73bd952a423a5e833

Please note that the first parameter of ```DynamicAppCall```  method should be the reversed contract script hash. 

```ontology contract invoke --address=2c2e3ab6a13134c6b2cf92e34d458c98332807f6 --params=string:StaticCallContract,[string:check,[int:0]] --gaslimit=200000 --gasprice=500```
or ```ontology contract invoke --address=2c2e3ab6a13134c6b2cf92e34d458c98332807f6 --params=string:StaticCallContract,[string:check,int:0] --gaslimit=200000 --gasprice=500``` 

coresponds with 

```angular2html
{
   "TxHash": "7c102f8000f19d4abb3f8721bac402c8d126089a738da413da6599fec9c72737",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "b16e976491982ddccd195dd73bd952a423a5e833",
         "States": [
            "31315f636865636b", //11_check
            "1027" //10000
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

```ontology contract invoke --address=2c2e3ab6a13134c6b2cf92e34d458c98332807f6 --params=string:DynamicCallContract,[bytearray:33e8a523a452d93bd75d19cddc2d989164976eb1,string:check,int:0] --gaslimit=200000 --gasprice=500```

coresponds with

```angular2html
{
   "TxHash": "fe87d192de5c5d3725150dafb91c2b787617c63b938e1b11f1366a87af09e427",
   "State": 1,
   "GasConsumed": 10000000,
   "Notify": [
      {
         "ContractAddress": "b16e976491982ddccd195dd73bd952a423a5e833",
         "States": [
            "31315f636865636b", //11_check
            "1027" //10000
         ]
      },
      {
         "ContractAddress": "2c2e3ab6a13134c6b2cf92e34d458c98332807f6",
         "States": [
            "6279746561727261793a20", //bytearray:
            "33e8a523a452d93bd75d19cddc2d989164976eb1"
         ]
      },
      {
         "ContractAddress": "2c2e3ab6a13134c6b2cf92e34d458c98332807f6",
         "States": [
            "3131315f44796e616d696343616c6c", // 111_DynamicCall
            "33e8a523a452d93bd75d19cddc2d989164976eb1",
            "636865636b", //check
            "00" //0
         ]
      },
      {
         "ContractAddress": "2c2e3ab6a13134c6b2cf92e34d458c98332807f6",
         "States": [
            "3232325f44796e616d696343616c6c",//222_DynamicCall
            "1027" //10000
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

