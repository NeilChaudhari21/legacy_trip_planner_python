import sys
from distutils.version import LooseVersion


def supports_runtime(minimum_version):
    current = ".".join(str(part) for part in sys.version_info[:3])
    return LooseVersion(current) >= LooseVersion(minimum_version)

