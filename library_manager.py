from typing import Union
import importlib
import os.path
from options import Options


class Library:
    def __init__(self, name: str, lib_data: dict, options: Options, module_data=None):
        self.__lib_data = lib_data
        self.__module_data = module_data
        self.__options = options
        self.__name = name

    @property
    def configuration(self) -> str:
        """
        Return configuration type

        Returns
        -------
        str
        """
        return self.__lib_data.get("configuration", "configure")

    @property
    def configure_params(self) -> list:
        """
        Return configuration parameters

        Returns
        -------
        str
        """
        return self.__lib_data.get("configure_params", [])

    @property
    def dependencies(self) -> list:
        """
        Return library dependencies

        Returns
        -------
        str
        """
        return self.__lib_data.get("dependencies", [])

    @property
    def download_params(self) -> list:
        """
        Return download parameters

        Returns
        -------
        str
        """
        return self.__lib_data.get("download_params", [])

    @property
    def folder_name(self) -> str:
        """
        Return library folder

        Returns
        -------
        str
        """
        return self.__lib_data.get("folder_name")

    @property
    def has_own_configuration(self) -> bool:
        """
        Check if library has it's own configuration

        Returns
        -------
        bool
        """
        if hasattr(self.__module_data, "has_own_configuration"):
            return getattr(self.__module_data, "has_own_configuration")()
        return hasattr(self.__module_data, "custom_configure")

    @property
    def name(self) -> str:
        """
        Return library name

        Returns
        -------
        str
        """
        return self.__name

    def add_configuration_params(self, *args) -> bool:
        """
        Add configuration parameter

        Returns
        -------
        bool
            Return True if success
        """
        if self.__lib_data.get("configure_params") is None:
            self.__lib_data["configure_params"] = list(args)
            return True
        self.__lib_data["configure_params"].extend(args)
        return True

    def add_dependencies(self, *args) -> bool:
        """
        Add configuration parameter

        Returns
        -------
        bool
            Return True if success
        """
        if self.__lib_data.get("dependencies") is None:
            self.__lib_data["dependencies"] = list(args)
            return True
        self.__lib_data["dependencies"].extend(args)
        return True

    def custom_configure(self):
        """
        Library own configuration
        """
        if not self.has_own_configuration:
            return
        func = getattr(self.__module_data, "custom_configure")
        kwargs = {}
        if "options" in func.__code__.co_varnames:
            kwargs["options"] = self.__options
        if "ctx" in func.__code__.co_varnames:
            kwargs["ctx"] = self
        func(**kwargs)

    def pre_configure(self):
        """
        Pre configure patch
        """
        if not hasattr(self.__module_data, "pre_configure"):
            return
        func = getattr(self.__module_data, "pre_configure")
        kwargs = {}
        if "options" in func.__code__.co_varnames:
            kwargs["options"] = self.__options
        if "ctx" in func.__code__.co_varnames:
            kwargs["ctx"] = self
        func(**kwargs)

    def post_configure(self):
        """
        Post configure patch
        """
        if not hasattr(self.__module_data, "post_configure"):
            return
        func = getattr(self.__module_data, "post_configure")
        kwargs = {}
        if "options" in func.__code__.co_varnames:
            kwargs["options"] = self.__options
        if "ctx" in func.__code__.co_varnames:
            kwargs["ctx"] = self
        func(**kwargs)

    def pre_dependency(self):
        """
        Preconfigure patch
        """
        if not hasattr(self.__module_data, "pre_dependency"):
            return
        func = getattr(self.__module_data, "pre_dependency")
        kwargs = {}
        if "options" in func.__code__.co_varnames:
            kwargs["options"] = self.__options
        if "ctx" in func.__code__.co_varnames:
            kwargs["ctx"] = self
        func(**kwargs)

    def post_install(self):
        """
        Post install patch
        """
        if not hasattr(self.__module_data, "post_install"):
            return
        func = getattr(self.__module_data, "post_install")
        kwargs = {}
        if "options" in func.__code__.co_varnames:
            kwargs["options"] = self.__options
        if "ctx" in func.__code__.co_varnames:
            kwargs["ctx"] = self
        func(**kwargs)

    def is_already_build(self) -> bool:
        """
        Check if library already build

        Parameters
        ----------
        lib_name: str
            The library name

        Returns
        -------
        bool
        """
        return os.path.exists(
            os.path.join(self.__options.target_dir, f"{self.name}.ok")
        )

    def is_needed(self) -> bool:
        """
        Check if library need to build or not

        Returns
        -------
        bool
        """
        if self.name not in self.__options.targets:
            return False
        if self.is_already_build():
            return False
        return True

    def mark_as_built(self) -> None:
        """
        Mark if the library has been build

        Returns
        -------
        None
        """
        filename = os.path.join(self.__options.target_dir, f"{self.name}.ok")
        with open(filename, "w", encoding="utf-8") as file:
            file.close()


class LibraryManager:
    """
    Manage build library
    """

    def __init__(self, library_data: dict, options: Options):
        self.__library = {}
        for lib in library_data:
            module_name = lib.replace("-", "_")
            patch = None
            if os.path.isfile(f"patch/{module_name}.py"):
                patch = importlib.import_module(f"patch.{module_name}")
            self.__library[lib] = Library(lib, library_data[lib], options, patch)

    def get_library(self, lib_name: str) -> Union[None, Library]:
        """_summary_

        Parameters
        ----------
        lib_name : str
            Library name

        Returns
        -------
        None
            If library not found
        Library
            Library class
        """
        return self.__library.get(lib_name)
