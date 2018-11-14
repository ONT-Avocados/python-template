The usage api can be found [here](https://apidoc.ont.io/smartcontract/#executionengine-entryscripthash).

ContractB script hash: 91396642e3ec943bf749eb858ec7edd118ee54be

ContractA script hash: 33b13425ec926402c7e8cd084755f3be7fff130f


When we invoke ```invokeA``` method within contractA.py, we get
```
{                                                                         
   "TxHash": "6859c8e7082f186706e68dba7af555522627758689b1a92ac5fb278e0c53
   "State": 1,                                                            
   "GasConsumed": 10000000,                                               
   "Notify": [                                                            
      {                                                                   
         "ContractAddress": "91396642e3ec943bf749eb858ec7edd118ee54be",   
         "States": [                                                      
            "3131315f696e766f6b6542",                                     
            "e703"                                                        
         ]                                                                
      },                                                                  
      {                                                                   
         "ContractAddress": "91396642e3ec943bf749eb858ec7edd118ee54be",   
         "States": [                                                      
            "0f13ff7fbef3554708cde8c7026492ec2534b133",                   
            "bf628f7045a3f4afa45b71794e92575c03b13579",                   
            "be54ee18d1edc78e85eb49f73b94ece342663991"                    
         ]                                                                
      },                                                                  
      {                                                                   
         "ContractAddress": "33b13425ec926402c7e8cd084755f3be7fff130f",   
         "States": [                                                      
            "3131315f696e766f6b6541",                                     
            "bf628f7045a3f4afa45b71794e92575c03b13579",                   
            "bf628f7045a3f4afa45b71794e92575c03b13579",                   
            "0f13ff7fbef3554708cde8c7026492ec2534b133"                    
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

When we invoke ```checkHash``` method within contractA.py, we get
```
{                                                                               
   "TxHash": "cfd59af87760c93942c2aa8dd3fbf1a1af9b0f74757a87cfd96320cb7674837c",
   "State": 1,                                                                  
   "GasConsumed": 10000000,                                                     
   "Notify": [                                                                  
      {                                                                         
         "ContractAddress": "33b13425ec926402c7e8cd084755f3be7fff130f",         
         "States": [                                                            
            "3131315f636865636b48617368"                                        
         ]                                                                      
      },                                                                        
      {                                                                         
         "ContractAddress": "33b13425ec926402c7e8cd084755f3be7fff130f",         
         "States": [                                                            
            "7d965ca196daa0abce0c0c3fc82d96f8ee15e96b",                         
            "7d965ca196daa0abce0c0c3fc82d96f8ee15e96b",                         
            "0f13ff7fbef3554708cde8c7026492ec2534b133"                          
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


