import os

# USAGE NOTES:
#
# Please update compiler paths according to your environment.
#
# It is not required to configure all supported compilers - any subset will work (even empty).
# It is okay to have entries with invalid paths for some compilers, they will be skipped.

compilers = {}

if os.name == 'nt':
    # Windows configuration example
    compilers = {
        'msvc'  : r'C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat',
        'dmd'   : r'C:\D\dmd2\windows\bin\rdmd.exe',
        'gdc'   : r'C:\D\gdc\bin\gdc.exe',
        'ldc'   : r'C:\D\ldc\bin\ldc2.exe',
        'go'    : r'C:\Go\bin\go.exe',
    }
else:
    # Linux/OS X configuration example
    compilers = {
        'gcc'   : r'/usr/bin/g++',
        'clang' : r'/usr/bin/clang++-3.6',
        'dmd'   : r'/usr/bin/rdmd',
        'gdc'   : r'/usr/local/gdc/bin/gdc',
        'ldc'   : r'/usr/local/ldc/bin/ldc2',
        'go'    : r'/usr/local/go/bin/go',
        'gccgo' : r'/usr/bin/gccgo',
    }
