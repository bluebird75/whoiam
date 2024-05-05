*The end of your indentation's nightmare*

by [Philippe Fremy](https://github.com/bluebird75/)

## Introduction

Indentation of external sources is a common problem. Some people use two
spaces, some four spaces, some tabulations, some (horror!) mix tab and
spaces. Text editors have usually options helping to deal with the way
you indent your files. Pressing tab will insert spaces of tabulations
depending on your settings. However, it only works properly with your
own files, which have been indented in your own way.

As soon as you start editing external sources, you are likely to face a
different indentation. Then your careful editor setting will simply fuck
up the file you edit unless the guy did use the same indentation as
yours. And you may not notice it. For example if I indent with tab but
sets them to be displayed as four columns and if I edit a file indented
with 4 spaces, all the lines I create will be indented with tab. They
will render fine on my editor, but probably not on someone else's
editor.

It is especially annoying if you program in python as the indentation is
part of the program structure.

I haven't found (yet) an editor that deals properly with this problem.
The solution however is simple: the text editor must find the
indentation used within a file and tune its settings according to this.
This is what Indent Finder does.

## Description

Indent Finder is a python script that reads a file and tells you what
indentation is used inside the file. The indentation analysis works on
any language. It was tested successfully with C, C++, python and Java
code.

The current version provides helps for the integration with vim. I hope
other editors will pick either the script or the idea, and that
auto-detecting indentation will become common amongst text editors. I am
releasing the code under the BSD License to encourage this.

The script is written in python because it was quick and easy way to
write it. The algorithm is pretty simple, and could be rewritten in C to
avoid the small (almost unnoticeable) delay due to the python
interpreter starting.

## Usage

### On the command line

In command line mode, it produces simple output like: space 4 or tab 8.
This output can by used in other programs or shell scripts.

    $ python indent_finder.py test_files/**/*.*
    ...
    test_files/mixed4/workshop.c : mixed tab 8 space 4
    test_files/mixed4/xpm_w32.c : mixed tab 8 space 4
    test_files/space2/TestRunner.cpp : space 2
    test_files/space4/cml.py : space 4
    test_files/space4/DebugClient.py : space 4
    test_files/space4/IOtest.java : space 4
    test_files/tab/diffmodel.cpp : tab 4
    test_files/tab/integration.c : tab 4
    test_files/tab/nbdebug.c : tab 4
    test_files/tab/pretty-make.py : tab 4
    test_files/tab/wsdebug.c : tab 4

### With Vim

All new opened buffer will be scanned by Indent Finder, which will set
the vim settings appropriately. The settings modified are: **shiftwidth,
tabstop, softtabstop and expandtab**. By default, all file types are
scanned but you may restrict this by editing the indent_finder.vim
script (a 5 line script).

When a file contains only tab, whether tabs are displayed are 2 columns,
4 columns or 8 columns is entirely a user preference. You must set it be
editing the value of DEFAULT_TAB_WIDTH in indent_finder.py .

You can see how IndentFinder set your vim settings by typing:

` :echo b:indent_finder_result`

To install IndentFinder:

1.  Edit the value of DEFAULT_TAB_WIDTH in indent_finder.py
2.  Install the python script (python setup.py install)
3.  Drop the file indent_finder.vim inside your vim plugin directory

## How it works

After trying different algorithm, the most reliable one seems to be:

-   scan all lines of the file
-   discard lines that may be improperly indented: empty lines, comment
    lines, lines following a \\
-   check how the line is indented compared to the previous line
-   if that indentation is composed of space, tab or tabs followed by
    space, then record that as an

indentation level.

-   at the end, compare which type of indentation has been used the
    most.

The algorithm ignores the first level of indentation (the one between no
indentation and indentation) because it is more often incorrect than
correct.

The algorithm can not find indentation of C header files, because such
files do not contain any meaningful indentation. This should not be a
problem, but be sure that indent_finder.py returns your preferred
default values in that case (see DEFAULT_RESULT at the beginning of
indent_finder.py ).

## License

Indent Finder is released under the BSD license.

## Download

### version 1.4 : 16 sep 2010

Changes:

-   Improvements to the heuristic, some file where incorrectly reported
    as tab
-   DEFAULT_OUTPUT is always returned when no decision can be made
    (fixes a bug).
-   Display the indentaion found in a comment of the vim output

Get it:

-   [Windows Version](http://labs.freehackers.org/attachments/download/396/indent_finder-1.4.zip):
    zip file
-   [Unix Version](http://labs.freehackers.org/attachments/download/397/indent_finder-1.4.tgz):
    tgz file

### version 1.31 : 7 sep 2008

Bug fix version: the vim plugin was not working correctly.

-   [Windows Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.31.zip):
    zip file
-   [Unix Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.31.tgz):
    tgz file

### version 1.3 : 20 jul 2008

Remove indent checker. Improve algorithm to detect mixed indentation
properly.

-   [Windows Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.3.zip):
    zip file
-   [Unix Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.3.tgz):
    tgz file

### version 1.2 : 16 nov 2007

Add Indent Checker script to check the indentation consistency of a
source tree.

-   [Windows Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.2.zip):
    zip file
-   [Unix Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.2.tgz):
    tgz file

### version 1.1 : 10 juil 2005

Improve heuristic by detecting indentation steps.

-   [Windows Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.1.zip):
    zip file
-   [Unix Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.1.tgz):
    tgz file

### version 1.0 : 22 nov 2002

Initial and stable release.

-   [Windows Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.0.zip):
    zip file
-   [Unix Version](http://www.freehackers.org/media/bluebird/indent-finder/indent_finder-1.0.tgz):
    tgz file

## Feedback

Indent Finder is developed by [Philippe Fremy](https://github.com/bluebird75/).

If IndentFinder ever reports wrong indentation, send me immediately a
mail, if possible with the offending file.

Suggestions, patch, I am open to feedback: Mail me.

## Other software by [Philippe Fremy](https://github.com/bluebird75/)

