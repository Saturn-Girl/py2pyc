import py_compile
import os
import ctypes

Read_DLL = True

if Read_DLL:
    if os.path.exists("data/discord-rpc.dll"):
        try:
            Function = ctypes.CDLL("data/discord-rpc.dll")
        except:
            Read_DLL = False
    else:
        print("dll not found")
else:
    Read_DLL = False

while True:
    script_name = input("enter the scirpt > ")
    if os.path.exists(script_name):
        py_compile.compile(script_name)
        print(f"compiled {script_name}")
    else:
        print(f"cannot find {script_name}")

