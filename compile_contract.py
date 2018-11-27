import binascii
from boa.compiler import Compiler

def hexlify_avm(blob):
    return binascii.hexlify(blob).decode('ascii')

def read_avm(filename):
    with open(filename, 'rb') as f:
        return hexlify_avm(f.read())

def save_avm(filename, a):
    with open(filename,'w') as f:
        f.write(a)


def run(file_path, file_name):
    """
    Read the source py file and compile it, save it into readable avm file
    :param file_path: the folder of file
    :param file_name: the source file name without ".py"-suffix
    :return:
    """
    template_file = template_file_path + template_file_name
    template_file_name_py = template_file + ".py"
    Compiler.load_and_save(template_file_name_py)
    # Out_readable_Avm.avm is the output file that we are going to use when deploying our contract
    readable_out_avm_file= template_file_path + "Out_readable_Avm.avm"
    save_avm(readable_out_avm_file, read_avm(template_file + ".avm"))


if __name__ == '__main__':
    """ set up the compiled file path and file name"""

    template_file_path = "./OEP4Sample/"
    template_file_name = "OEP4Sample"

    # template_file_path = "./OEP5Sample/"
    # template_file_name = "OEP5Sample"


    # template_file_path = "./MigrateDestruct/"
    # template_file_name = "migrate_destroyWithinContract"

    # template_file_path = "./Static_Call_Oep4/"
    # template_file_name = "static_call_Oep4"

    # template_file_path = "./Storage_Example/"
    # template_file_name = "storage_example"

    # template_file_path = "./Struct_Example/"
    # template_file_name = "struct_example"

    # template_file_path = "./NativeAssetInvoke/"
    # template_file_name = "native_asset_invoke"

    # template_file_path = "./EventTest/"
    # template_file_name = "event_test"

    # Compile the designated file.py
    run(template_file_path, template_file_name)




