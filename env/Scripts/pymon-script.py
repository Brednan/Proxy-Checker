#!"d:\desktop\python desktop apps\proxy-checker\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'py-mon==1.1.0','console_scripts','pymon'
__requires__ = 'py-mon==1.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('py-mon==1.1.0', 'console_scripts', 'pymon')()
    )
