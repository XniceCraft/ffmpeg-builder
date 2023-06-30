"""
Contains build data
"""
from dataclasses import dataclass
import os


@dataclass
class Options:
    """
    Contains build data
    """

    targets: list
    threads: int = 1
    silent: bool = False
    target_dir: str = "target"
    release_dir: str = "release"
    bin_dir: str = "bin"
    extra_cflags: str = ""
    extra_ldflags: str = ""
    extra_libs: str = ""
    extra_ffmpeg_args: str = ""
    static_ffmpeg: bool = False
    nonfree_build: bool = False

    def __post_init__(self):
        if not self.target_dir.startswith("/"):
            self.target_dir = os.path.join(os.getcwd(), self.target_dir)
        if not self.release_dir.startswith("/"):
            self.release_dir = os.path.join(os.getcwd(), self.release_dir)
