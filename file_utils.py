"""Utilities for modifying file"""
from pathlib import Path
from shutil import rmtree
from typing import Union
import os
import os.path


def delete_lines(file_path: str, start: int, end: int) -> bool:
    """
    Function to delete lines in the file from specific
    start and specific end

    Parameters
    ----------
    file_path: str
        File path in form of string
    start: int
        Start line
    end: int
        End line

    Returns
    -------
    bool
        Return True if success
    """
    with open(file_path, encoding="utf-8") as file:
        file_read = file.readlines()
        file.close()
    with open(file_path, "w", encoding="utf-8") as file:
        for index, value in enumerate(file_read):
            if index < start or index > end:
                file.write(value)
        file.close()
    return True


def find_string(file_path: str, text: str) -> Union[None, int]:
    """
    Find string in file and return the index

    Parameters
    ----------
    file_path: str
        File path in form of string
    text: str
        Text that you wanna find

    Returns
    -------
    None
        If text not found in file
    int
        If text founded in the file
    """
    with open(file_path, encoding="utf-8") as file:
        index = 0
        for value in file:
            if text in value:
                file.close()
                return index
            index += 1
    return None


def mkdir(dir_path: str) -> Union[None, bool]:
    """
    Create directory

    Parameters
    ----------
    dir_path: str
        Directory path

    Returns
    ------
    None
        If directory already exists
    True
        If success to create folder
    False
        If failed to create folder
    """
    if os.path.exists(dir_path):
        print(f"Directory {dir_path} already exists, can't create")
        return None
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    if os.path.exists(dir_path):
        print(f"Directory {dir_path} created successfully")
        return True
    print(f"Directory {dir_path} can't be created")
    return False


def replace(file_path: str, old: str, new: str) -> bool:
    """
    Replace content inside file

    Parameters
    ----------
    file_path: str
        File path in form of string
    old: str
        Old content
    new: str
        New content

    Returns
    -------
    bool
        Return True if success
    """
    with open(file_path, encoding="utf-8") as file:
        old_file = file.read()
        file.close()
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(old_file.replace(old, new))
        file.close()
    return True


def remove(path: str) -> Union[None, bool]:
    """
    Remove file or directory

    Parameters
    ----------
    path: str
        File or directory path

    Returns
    -------
    None
        If file or directory not found
    True
        If file or directory success to remove
    False
        If file or directory failed to remove
    """
    if not os.path.exists(path):
        print(f"{path} doesn't exist, no need to remove it")
        return None
    if os.path.isdir(path):
        rmtree(path, ignore_errors=True)
        if os.path.exists(path):
            print(f"Directory {path} still exists, can't remove")
            return False
        print(f"Directory {path} removed successfully")
        return True
    os.remove(path)
    if os.path.exists(path):
        print(f"File {path} still exists, can't remove")
        return False
    print(f"File {path} removed successfully")
    return True
