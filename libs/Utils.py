# -*- coding: utf-8 -*-"""
"""
You can import this file and methods in your smart contract,
you can also add utility methods within this function based on your needs.
"""
from boa.interop.System.Storage import Delete, Put

def Revert():
    """
    Revert the transaction. The opcodes of this function is `09f7f6f5f4f3f2f1f000f0`,
    but it will be changed to `ffffffffffffffffffffff` since opcode THROW doesn't
    work, so, revert by calling unused opcode.
    """
    raise Exception(0xF1F1F2F2F3F3F4F4)

def SafePut(context, key, value):
    if value == 0:
        Delete(context, key)
    else:
        Put(context, key, value)


