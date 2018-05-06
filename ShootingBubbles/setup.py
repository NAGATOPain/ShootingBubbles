import sys
from cx_Freeze import setup, Executable

setup(
    name = "Shooting Burbles - NTL",
    version = "1.0",
    description = "A clone of asteroids game.",
    executables = [Executable("main.py", base = "Win32GUI")])