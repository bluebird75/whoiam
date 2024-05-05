*A brick game*

by [Philippe Fremy](https://github.com/bluebird75/)

## Introduction

Klotski is small brick game which has its root in a wooden game named
(in french) *Ane rouge*. The goal is to bring the red piece to its
destination by moving other pieces. It sounds simple but it is a real
brainteaser.

There was a klotski game on Windows 3.1, and this is were all levels are
from. There is also a basic gnome version of klotski here. I had a look
at it before starting Klotski, so some design ideas have probably
slipped from there :-)

## Screenshot

![](http://www.freehackers.org/media/bluebird/klotski/screenshots/klotski-screenshot.png)

## Requirements

On Linux, you need [Python](http://www.python.org),
[Qt](http://www.trolltech.com) and
[PyQt](http://www.thekompany.com/projects/pykde/). On Windows,
everything works by itself :-).

## History

Klotski is written in [Python](http://www.python.org) and uses the
[PyQt](http://www.thekompany.com/projects/pykde/) binding developped by
Phil Thompson, to take advantage of the QCanvas from
[Qt](http://www.trolltech.com).

This is my first program using python and PyQt. I must say I have
enjoyed it a lot: Python and Qt are both excellent, easy to use and well
documented. I have never been able to implement my ideas so quickly. The
usual cycle *think, organise into organigram, code, compile, correct
compiling errors, run, correct bugs, run, it work* was reduced to
*think, code, run, it works*. Because of the simplicity and the power
the python language, my ideas could be expressed very clearly and I
could concentrate on what I wanted to do instead of how I needed to code
it. The result is a simple and clean program, that was coded in half the
time (and probably less) it would have taken to do it in C++.

## Download

### version 1.2 : 01 june 2006

-   Windows version with installer:
    [Setup-Klotski-1.2-20060601.exe](http://www.freehackers.org/media/bluebird/klotski/Setup-Klotski-1.2-20060601.exe)

### version 1.1: 17 november 2004

-   Unix version:
    [klotski-1-1.tar.bz2](http://www.freehackers.org/media/bluebird/klotski/klotski-1-1.tar.bz2)
-   Windows Version with installer:
    [Setup-Klotski-1.1-20050416.exe](http://www.freehackers.org/media/bluebird/klotski/Setup-Klotski-1.1-20050416.exe)

### version 1.0 : 23 january 2001

-   Unix version:
    [klotski-1.0.tar.bz2](http://www.freehackers.org/media/bluebird/klotski/klotski-1.0.tar.bz2)
-   Windows version (no installer):
    [klotski-1.0.zip](http://www.freehackers.org/media/bluebird/klotski/klotski-1.0.zip)

## Feedback

I'm always interested in feedback, either good or bad. What would really
interest me are contributions of new boards. Don't hesitate to [contact me](Contact_Bluebird).

You can also contribute to klotski. Look at the file boards.kts, it
contains the description of the board in a simple format. Adding a new
board is quite easy.

## Solution

Due to many requests, I have put-up a solution of the most difficult
puzzle, the dreaded *Ane Rouge*: [the solution](Philippe/Klotski_Solution_of_Ane_Rouge).

Look at it only when you start to get desperate (this is, after at least
one month of effort). It took me something like one month to find it.
The real tricky part is the end: you have to make the red square change
side else it won't go out.

## Related links

-   [Bricks Games](http://www.bricks-game.de), a very good sliding tile
    game with many levels and special pieces, web ranking, puzzles
    everymonth and very good things.
-   [Glotski](http://gfpoken.bigw.org/glotski/) , a Gnome equivalent

## Other software by [Philippe Fremy](https://github.com/bluebird75/)

