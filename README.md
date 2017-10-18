# wotdisttools

Provides Python setuptools command `bdist_wotmod` to package any setuptools
based project into a World of Tanks’ wotmod package.

The main use cases for this command are:

* Packaging game mods into wotmod packages.
* Packaging any setuptools based Python packages (e.g. those found from PyPI)
  into wotmod packages, providing easier usage and distribution of 3rd party
  libraries for game mods.

There are certain limitations though:

* Only pure Python projects are supported, World of Tanks often just crashes
  when it tries to load native pyd files
* MANIFEST and MANIFEST.in are not processed
* Executable scripts are not installed
* Distutils based setup.py script are not supported
* Loading of data files may not work unless the project is specifically designed
  to use ResMgr to load them

Some of these limitations exist because I didn't need them and was too lazy to
add them. If you need more functionality, let me know.

Implementation of the command is based on packages specification from:
  https://koreanrandom.com/forum/topic/36987-/

The specification is also available in `docs` subdirectory.

## Getting Started

These instructions will get you a copy of the project up and installed to your
local machine.

### Prerequisites

You will need Python 2.7 to compile py files. Using any other version might
produce pyc files which are incompatible with World of Tanks’ embedded Python
interpreter. Setuptools and Pip are also required, but they should come included
with Python. Just upgrade them first to latest versions:

```powershell
python -m pip install -U pip setuptools
```

### Installing

Clone this repository first and then install it using setuptools script:

```powershell
git clone wotdisttools https://github.com/jhakonen/wotdisttools.git
cd wotdisttools
python setup.py install
```

Once installed, any Python project which has setuptools based setup.py will have
a new command `bdist_wotmod` which you can use to create a wotmod package out of
the project.

```powershell
python setup.py bdist_wotmod --help
```
```
...
Options for 'bdist_wotmod' command:
  --bdist-dir (-d)   temporary directory for creating the distribution
  --dist-dir (-d)    directory to put final built distributions in
  --author-id        developer's nickname or website (f.e. com.example)
                     [default: setup author or maintainer]
  --mod-id           modification identifier [default: setup name]
  --mod-version      modification version [default: setup version]
  --mod-description  modification description [default: setup description]
  --version-padding  number of zeros to use to pad each version fragment
                     [default: 2]
  --install-lib      installation directory for module distributions [default:
                     'res/scripts/client/gui/mods']
  --install-data     installation directory for data files [default:
                     'res/mods/<author_id>.<mod_id>']
...
```

### Examples

For packaging a World of Tanks mod into a wotmod package, use command:

```powershell
python setup.py bdist_wotmod
```

This will create a new wotmod file to `dist` subdirectory.
All Python py/pyc files are stored to `res/scripts/client/gui/mods` within the
wotmod package. Any data files will end up to wotmod's
`res/mods/<author_id>.<mod_id>` directory.

For packaging non-mod 3rd party libraries, use commands:

```powershell
pip download <package name> --no-binary :all:
```

Extract downloaded file somewhere, cd to its directory and give command:
```powershell
python setup.py bdist_wotmod --install-lib=res/scripts/common
```

This will create a wotmod archive which has the project's Python packages
located on PYTHONPATH where they are easier to import when needed (and some
libraries will not even work if they are not on PYTHONPATH).

You may also want to set package's author-id with `--author-id=<name>` to a more
descriptive value.

## Running tests

Unit tests are executed with command:

```bash
python setup.py test
```

## License
This project is licensed under the MIT License - see the LICENSE file for
details.
