import platform
from pathlib import Path

from PyKCS11 import PyKCS11Lib

from .exceptions import PlatformNotSupported

# prebuild opensc libraries
OPENSC_LIBS_PATHS = {
    'Darwin-64bit': 'opensc/opensc-pkcs11-Darwin-64bit.so',
    'Windows-64bit': 'opensc/opensc-pkcs11-Windows-64bit.dll',
    'Windows-32bit': 'opensc/opensc-pkcs11-Windows-32bit.dll'
}

# https://github.com/easybuilders/easybuild/wiki/OS_flavor_name_version
# One of ['Windows', 'Darwin', 'Linux']
_SYSTEM = platform.system()
# One of ['32bit' , '64bit'] - depends on python executable
_ARCHITECTURE = platform.architecture()[0]

PLATFORM = '{}-{}'.format(_SYSTEM, _ARCHITECTURE)

# opensc-pkcs11 lib absolute path
OPENSC_LIB_PATH = Path(__file__).parent / OPENSC_LIBS_PATHS.get(PLATFORM, '')

if not OPENSC_LIB_PATH.is_file():
  raise PlatformNotSupported(
      'opensc-pkcs11 library for platform {} is not included'.format(PLATFORM))


PKCS11 = PyKCS11Lib()
PKCS11.load(str(OPENSC_LIB_PATH.resolve()))