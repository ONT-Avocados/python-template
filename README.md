This project aims for providing demos in python version for developing smart contract based on ontology.
The following templates have been tested smoothly. The template contracts all work well 
and they can be used as reference when you write ONT smart contract. 

* libs contain safe SafeMath, SafeCheck and Utils files
* migrate_destroyWithinContract.py
* MySimpleToken.py
* static_call_Oep4.py
* struct_example.py
* storage_example.py
* native_asset_invoke.py
* OEP4Sample.py
* OEP5Sample.py
* event_test.py

## Instruction

###  Preparation

##### 1. configure ontology cli
For test usage, you can start ontology node and test your contract under ontology cli. 
###### 1.1 Install ontology cli
 The instructions for installation of cli is given [here](https://github.com/ontio/ontology).

###### 1.2 Usage of ontology cli
The instructions for usage of cli is given here ([EN](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide.md), [CN](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide_CN.md)).
  


##### 2. configure neo-boa environment
Note here that the official installation instruction is a little bit misunderstanding.
 Here I will give the full and correct installation guide.

##### 2.1. Download  [neo-boa (ONT version)](https://github.com/ontio/neo-boa)

##### 2.2. Make a Python 3 virtual environment and activate it (in windows system) via:

```
python3 -m venv venv
cd venv/bin
activate
```
##### 2.3. Then, install the requirements:

```
pip install -r requirements.txt
```

##### 2.4. Installation requires a Python 3.6 or later environment.

```
pip install neo-boa
```

##### 2.5. You can read the [docs](https://neo-boa.readthedocs.io/en/latest/) about how to use neo-boa

Suggest you can ignore boa-test since some of the paths are configured wrongly.
 

###  Usage

Download the "python-template" zip folder and unzip it to any folder you create parallel with "boa" folder.
##### 3.1 Compile contract
Open "compile_contract.py", make sure there is nothing wrong with compiling it. Then you can run this py file. 
Accordingly, the corresponding readable avm file will be in the corresponded folder.

Copy your avm file into your "$GOPATH/src/github.com/ontio/ontology/*" (the folder containing your ontology and wallet).
##### 3.2 Start ontology node
```
ontology --testmode --gasprice=0
```
##### 3.3 Deploy contract
Deploy smart contract in testmode. Here --code="your avm file"
```
./ontology contract deploy --name=xxx 
--code=xxx 
--author=xxx --desc=xxx --email=xxx --needstore --gaslimit=100000000

```
##### 3.4 Invoke contract
Invoke methods within your contract, please refer to the usage of ontology cli ([EN](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide.md), [CN](https://github.com/ontio/ontology/blob/master/docs/specifications/cli_user_guide_CN.md)).

 