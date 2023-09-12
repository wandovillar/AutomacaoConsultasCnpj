import sys
from cx_Freeze import setup, Executable

# Inclua todas as dependências necessárias (módulos importados) aqui
includes = []

# Crie o executável
executables = [
    Executable('ConsultasCnpj.py', base=None)
]

# Configurações para a construção do executável
build_exe_options = {
    "includes": includes,
    "excludes": [],
    "packages": [],
    "include_files": [],
}

setup(
    name="ConsultasCnpj",
    version="1.0",
    description="Capturar informa",
    options={
        "build_exe": build_exe_options,
    },
    executables=executables
)
