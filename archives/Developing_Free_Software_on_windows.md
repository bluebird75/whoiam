You are a linux freak, but for some reason, you need to develop on
windows. First of all, check [Surviving on Windows](archives/Surviving_on_Windows) for a list of software to
install, that will make you feel a bit more at home.

## Cygwin

You can compile and link on cygwin, even use a XServer. The libraries
are a port of unix libraries, with a unix emulation layer, provided by a
cygwin DLL. The advantage is that it is very easy to port a unix
program, since you don't run into any obstacle of windows.

The problem is that all your executables or DLL will depend on the
cygwin DLL. Graphical programs may need the XServer to be running.

## Mingw

[Mingw](http://www.mingw.org/wiki/Getting_Started) is:

-   gcc compiler
-   make
-   windows development headers for windows libraries

This means that you can compile a windows program with mingw. The
windows headers will make your program depend on windows libraries, such
as mscvcrt.dll . The resulting program or dll looks like a native
windows dll and could be used by to link with Visual Studio.

Mingw does not provide any help to port a unix program to windows. It
does save you the trouble of using Visual Studio.

## MSYS

[MSYS](http://www.mingw.org/wiki/MSYS) is not a simple beast in itself.
It comes as different packages:

### <i>Bare</i> MSYS

I added the <i>bare</i>, the regular name is just msys. This contains a
minimal set of tools needed to run a ./configure script. This does not
contain a compiler. The tools are:

-   bash
-   rxvt
-   cp, diff, gzip, head, sed, ...

So, with <i>Bare</i> MSYS and mingw, you can build a native windows
application with no other dependency than windows regular DLL.

### MSYS Developer - msysDVLPR

This is a compilation suite to compile applications that will depend on
the msys dll. So, using this package, you get a situation very similar
to the situation of cygwin.

### MSYS Developer Toolkit - msysDTK

MSys developer toolkit is a set of tools for easy development, which
depend on the MSys DLL. So, again, we get something very similar to the
cygwin situation.

## GnuWin32

Another one. This one provides common unix tools in native form for
windows. The tools of GnuWin32 package do not depend on any msys or
cygwin DLL.

In one sense, GnuWin32 is the continuation of bare msys.

The packages of GnuWin32 are very clean: man pages inside a pdf,
installation in the windows start menu, ...
