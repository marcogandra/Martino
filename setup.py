from cx_Freeze import setup, Executable
 
setup(
    name="Diario_mmrj",
    version = "2.5.0",
    description = ".py to .exe",
    executables = [Executable("diario.py")])

