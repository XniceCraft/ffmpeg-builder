# pylint: disable = C0114
from platform import system
import file_utils


def pre_configure():
    """
    Pre configuration build patch
    """
    if system() == "Darwin":
        file_utils.replace("build/make/Makefile", "--version-script", "")
        file_utils.replace(
            "build/make/Makefile",
            "-Wl,--no-undefined -Wl,-soname",
            "-Wl,-undefined,error -Wl,-install_name",
        )
