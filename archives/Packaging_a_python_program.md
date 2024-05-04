The goal is to take an existing python program and distribute it as a
self-contained executable, that does not require python are any python
module to be installed. Of course, this is more suitable on Windows than
on Linux but it can actually serves both platforms. Even on linux,
source is not necessarily the best distribution mean for a program to
\*just work\*.

Misc thoughts:

-   You can use a full blown installer under windows, either as a
    replacement or as a complement. We have a specific page for this :
    [Windows installer](Windows_installer)
-   [waf](https://en.wikipedia.org/wiki/Waf_(build_system)) has its own method,
    [described here](http://waf-devel.blogspot.com/2010/02/storing-binary-data-in-python-files.html)

### [Py2exe](http://www.py2exe.org/)

-   windows only
-   support for com servers, nt services and all the other windows
    stuff.
-   reasonably well documented, works well.
-   manage binary dependancies
-   can pack into exe+dll or into single exe which automatically
    extracts dll at runtime

**Bluebird's opinion:**

*I have used it for years on several projects. Works like a charm, very
easy to use.*

### [PyInstaller](http://pyinstaller.python-hosting.com/)

-   windows and unix (and Mac in the svn trunk)
-   no support for zipfile import (introduced in python 2.3), so even
    works with python 1.5.
-   can package data files inside your executable.
-   manage binary dependancies on linux
-   can encrypt the final program
-   in linux, does its best to make it run on any linux distro
-   one-file mode, where everything is packed inside the executable:
    data, sourcecode, dll/so

**Bluebird's opinion:**

''I have used it for PyTiCroque and it was also
very easy to use and works like charm. I like the idea that I can also
use it on Linux.

The SVN version is much more advanced than the last released version. It
has MacOs support and more nice stuff. ''

### [cx_Freeze](http://cx-freeze.sourceforge.net/)

-   windows and linux
-   zipfile import support
-   no binary dependancies handling on linux

### [bbfreeze](http://cheeseshop.python.org/pypi/bbfreeze/0.95.2)

-   windows and linux
-   zipfile import support
-   manage binary dependancies on linux

bbfreeze is the only one, which handles eggs and zipfile imports
transparently (and therefore also provides a mechanism for including
data files using setuptools pkg_resources module).

### [py2app](http://undefined.org/python/#py2app)

-   MacOs X only
