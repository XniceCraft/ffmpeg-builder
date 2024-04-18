# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/FFmpeg_icon.svg/480px-FFmpeg_icon.svg.png" width="35px"> FFmpeg Builder

## About
Build FFmpeg from scratch with Python!

This work is inspired by [ffmpeg-build-script](https://github.com/markus-perl/ffmpeg-build-script/blob/master/build-ffmpeg). Markus did a great job on gathering requirements for multiple components. But I can't use it because of Bash. Bash is a real shit: fragile syntax, no debug, no IDE, no error reporting.

Forked from https://github.com/openstreamcaster/ffmpeg-builder

## Usage

* Build:`python3 build.py --build`
* Clean:`python3 build.py --clean`
* Help:`python3 build.py --help`

## Operating systems

- GNU/Linux
- MacOS
- Windows (MSYS2)

## Windows

Windows is a very unfriendly place. Unfortunately, it's the only place with games.
Don't trust Windows build, and it needs in-depth testing.
Nonetheless, here are the steps to build:

1) [Install MSYS2](https://www.msys2.org/). It's like ArchLinux, but with Windows Kernel. Follow all steps, update everything as the page says.
2) Cast this magic spell to set up environment: `pacman -S --needed base-devel mingw-w64-i686-toolchain mingw-w64-x86_64-toolchain mingw-w64-i686-cmake mingw-w64-x86_64-cmake mingw-w64-x86_64-llvm mingw-w64-x86_64-clang`
3) Install Python `pacman -S python3 mingw-w64-x86_64-python3-pip` and run `pip3 install plumbum`
4) Run `python3 build.py --build` as usual and pray your gods.

## License

Universal Permissive License, as in LICENSE.md in this repository.

> The UPL is a lax, non-copyleft license that is compatible with the GNU GPL. The UPL contains provisions dealing explicitly with the grant of patent licenses, whereas many other simple lax licenses only have an implicit grant. 
© [Free Software Foundation](https://www.fsf.org/blogs/licensing/universal-permissive-license-added-to-license-list)

Short hint: you may use it in your Apache 2 or GPL projects, but there's a lot of nuances and implications, so please ask professional help if you don't understand anything about licensing.
