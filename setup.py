import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"



setup(  name = "music_player",
        version = "1.0",
        description = "sarcino music_player",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, icon="icon.ico")])