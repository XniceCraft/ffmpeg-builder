"""
Contains utiltt for building ffmpeg
"""
# pylint: disable=line-too-long
import logging
import platform
import re
import sys
import plumbum

logger = logging.getLogger(__name__)


def add_path(dir_path: str, take_priority: bool = True) -> None:
    """
    Add directory to PATH env

    Parameters
    ----------
    dir_path: str
        Directory path
    take_priority: bool (default True)
        If true, the directory will be prioritized

    Returns
    -------
    None
    """
    old_path = plumbum.local.env["PATH"]
    plumbum.local.env["PATH"] = (
        f"{dir_path}:{old_path}" if take_priority else f"{old_path}:{dir_path}"
    )


def command_exists(cmd: str) -> bool:
    """
    Check if commands exist

    Parameters
    ----------
    cmd: str
        Command name

    Returns
    -------
    bool
    """
    try:
        plumbum.local.which(cmd)  # pylint: disable=pointless-statement
        return True
    except plumbum.commands.CommandNotFound:
        return False


def run_fg(command: str, *args, silent: bool = False) -> bool:
    """
    Run command at foreground

    Parameters
    ----------
    command: str
        Command
    *args
        Command additional argument
    silent: bool
        Print foreground result or not

    Returns
    -------
    bool
    """
    try:
        cmd = plumbum.local[command][args]
        result = cmd.run() if silent else cmd & plumbum.TEE
        return result
    except plumbum.commands.CommandNotFound:
        logger.exception("Command %s not found!", command)
        return False
    except plumbum.commands.ProcessExecutionError as err:
        logger.exception(err)
        return False


def require_commands(*commands) -> None:
    """
    Check if required commands exist

    Parameters
    ----------
    *commands
        List of commands

    Returns
    -------
    None
    """
    absent_commands_list = [
        command for command in commands if not command_exists(command)
    ]
    if absent_commands_list:
        absent = ", ".join(absent_commands_list)
        print(f"Required commands not found: {absent}")
        sys.exit(1)


def path_fixer(src: str) -> str:
    """
    Converting windows path to unix style path

    Parameters
    ----------
    src: str
        Windows path

    Returns
    -------
    str
        Unix style path

    Raises
    ------
    NotImplementedError
        Raised if path doesn't match any pattern

    Information
    -----------
    The following code is the poor's man implementation of this:
    https://stackoverflow.com/questions/41492504/how-to-get-native-windows-path-inside-msys-python
    It's working, but maybe we should consider to switch to the full version
    """
    if platform.system() != "Windows":
        return src

    # Handle Windows (native path)
    path_search = re.search("([a-zA-Z]):/(.*)", src, re.IGNORECASE)
    if path_search:
        drive = path_search.group(1).lower()
        path = path_search.group(2)
        result = f"/{drive}/{path}"
        return result
    # Handle Windows (native path with backward slashes)
    # Actually we can skip this, but it's useful for validation
    path_search = re.search(r"([a-zA-Z]):\\(.*)", src, re.IGNORECASE)
    if path_search:
        drive = path_search.group(1).lower()
        path = path_search.group(2).replace("\\", "/")
        result = f"/{drive}/{path}"
        return result
    # Handle Windows (MSYS2, Git Bash, Cygwin, etc)
    simulated_path_search = re.search("/([a-zA-Z])/(.*)", src, re.IGNORECASE)
    if simulated_path_search:
        drive = simulated_path_search.group(1).lower()
        path = simulated_path_search.group(2)
        result = f"/{drive}/{path}"
        return result
    # No sense in continuing without properly parsed path
    raise NotImplementedError


def configure(prefix: str, *args, **kwargs) -> bool:
    """
    Run configure

    Parameters
    ----------
    prefix : str
        Build prefix

    Returns
    -------
    bool
        Return True if success
    """
    configure_flags = ("./configure", f"--prefix={prefix}") + args
    logger.debug("Configuring with configure. Command: %s", "".join(configure_flags))
    if platform.system() == "Windows":
        configure_flags = ("bash",) + configure_flags
    run_fg("chmod", "+x", "./configure")
    if not run_fg(*configure_flags, **kwargs):
        sys.exit(1)
    logger.debug("Configure with configure done!")
    return True


def cmake(prefix: str, *args, **kwargs) -> bool:
    """
    Run cmake

    Parameters
    ----------
    prefix : str
        Build prefix

    Returns
    -------
    bool
        Return True if success
    """
    cmake_flags = (
        "cmake",
        "-DCMAKE_BUILD_TYPE=Release",
        f"-DCMAKE_INSTALL_PREFIX={prefix}",
        f"-DCMAKE_PREFIX_PATH={prefix}",
    ) + args
    logger.debug("Configuring with cmake. Command: %s", "".join(cmake_flags))
    if platform.system() == "Windows":
        cmake_flags += ("-G", "MSYS Makefiles")
    if not run_fg(*cmake_flags, **kwargs):
        sys.exit(1)
    logger.debug("Configure with cmake done!")
    return True


def make(threads: int, *args, **kwargs) -> None:
    """
    Make command

    Parameters
    ----------
    threads: int
        How many threads
    *args
        Will be passed to fg function
    **kwargs
        Will be passed to fg function

    Returns
    -------
    None
    """
    if not run_fg("make", f"-j{threads}", *args, **kwargs):
        sys.exit(1)


def make_install(*args, **kwargs) -> None:
    """
    Make install

    Parameters
    ----------
    *args
        Will be passed to fg function
    **kwargs
        Will be passed to fg function

    Returns
    -------
    None
    """
    if not run_fg("make", "install", *args, **kwargs):
        sys.exit(1)


def meson(prefix: str, *args, **kwargs) -> bool:
    """
    Run meson

    Parameters
    ----------
    prefix : str
        Build prefix

    Returns
    -------
    bool
        Return True if success
    """
    meson_flags = (
        "meson",
        "setup",
        f"--prefix={prefix}",
    ) + args
    logger.debug("Configuring with meson. Command: %s", "".join(meson_flags))
    if not run_fg(*meson_flags, **kwargs):
        sys.exit(1)
    logger.debug("Configure with meson done!")
    return True


def ninja(threads: int, **kwargs) -> bool:
    """
    Run ninja

    Parameters
    ----------
    threads : int
        How many threads to run ninja

    Returns
    -------
    bool
        Return True if success
    """
    if not run_fg("ninja", "-j", threads, **kwargs):
        sys.exit(1)
    if not run_fg("ninja", "install", **kwargs):
        sys.exit(1)
    return True
