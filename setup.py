from cx_Freeze import executable, setup, Executable
from cx_Freeze.dist import build_exe


setup(
    name='Proxy Checker',
    version='1',
    description="Check lists of proxies by checking if they successfully connect to the URL you specify",
    executables=[Executable('GUI.py', base='Win32GUI')]
)