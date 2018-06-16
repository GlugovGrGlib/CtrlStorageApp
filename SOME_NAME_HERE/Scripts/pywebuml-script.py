#!c:\django-project\agrusapp\agrus\some_name_here\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pywebuml==0.3.0','console_scripts','pywebuml'
__requires__ = 'pywebuml==0.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pywebuml==0.3.0', 'console_scripts', 'pywebuml')()
    )
