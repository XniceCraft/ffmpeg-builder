import os.path
from file_utils import remove, replace


def pre_configure():
    """
    Pre configuration build patch
    """
    remove(os.path.join("Modules", "FindJava.cmake"))
    replace(
        "Tests/CMakeLists.txt",
        "get_filename_component.JNIPATH",
        "#get_filename_component(JNIPATH",
    )
