import sys
from cx_Freeze import *
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning
build_exe_options = {"packages": ["os"]}



setup(  name = "music_player",
        version = "1.0",
        description = "sarcino music_player",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base="Win32GUI")])