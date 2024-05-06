
by [Philippe Fremy](https://github.com/bluebird75/)

## Introduction

This program is probably obsolete. It was developed in 2001 on a hot
summer to prevent my computer to overheating while doing gentoo
compilations. The program depends strongly on the output of lmsensors,
as it existed at that time, on my specific computer. It's very likely
that it won't work today on a linux computer but feel free to try ! I
have not heard of any valid replacement for this task, if you know about
one, tell me !

On my dual-CPU gentoo linux system and I have discovered a big problem:
in my attempts to reduce the sound of the CPU fans, I lost a lot of
cooling power. Now, everytime I emerge a new software, my CPU
temperatures raises to 60 and sometimes 70 degrees. The CPUs are still
alive (thanks Intel) but the computer tends to freeze easily.

After some thinking, I developed the counter-weapon to this geeky
problem: the *keep cool* script. The idea is quite simple: watch the
temperature. If it gets too high, just sleep the responsible process and
wait until things cool down.

## Description

Keep Cool is a small python script that watches the temperature of your
system, and sleep processes taking too much CPU when this temperatures
rises above a given limit. I wrote it to solve my problem and publish it
here in the hope that it helps solve some of yours. However, there is no
guarantee of anything.

## How it works

The temperature is parsed from the output of
[lmsensors](http://www.lm-sensors.org). You might have to customise that
a bit to match the output of your system. I am okay to help if don't
know any python coding.

The most CPU consuming process is read from the output of ps, which
might also be different on your system given the wide number of ps
implementation and option set.

The script has to run with enough privileges to send stop and continue
signals to the process taking the CPU. In case of Gentoo emerging, I run
it as root also it might probably be possible to achieve the same effect
with just the portage user rights. If somebody has a better proposal, I
am ready to accept it. It might be a good idea to rewrite it in C to
avoid running python program as root but I am just too lazy.

When a process is stopped, keep cool waits until the temperature gets
down again. It then restarts the processes one by one.

There is a bunch of variables at the beginning of the script, that you
can customise to your needs: the highest allowed temperature, the low
temperature after which processes are restarted, the delay between two
temperature check.

## Screenshot

KeepCool in action :

```
   werewindle /home/philippe/python/keepcool # python keepcool.py
   22:42:13 CPU are above max temperature :  53.1
   process stopped:  15046 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1plus -
   1 process currently stopped
   22:42:58 Temperature is down again :  47.6 49.7
   Restarting  15046 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1plus -
   22:43:28 CPU are above max temperature :  53.1
   process stopped:  16130 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1plus -
   process stopped:  16265 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1 -fpre
   2 process currently stopped
   22:43:43 Temperature is down again :  46.7 49.6
   Restarting  16130 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1plus -
   22:43:48 Temperature is down again :  48.7 49.7
   Restarting  16265 /usr/lib/gcc-lib/i686-pc-linux-gnu/3.2.3/cc1 -fpre
```

As you can see, the summer was really hot in France.

## Download

The script is available at:
[keepcool.py](keepcool.py).

## Usage

You need [lmsensors](http://www.lm-sensors.org) to be installed.

Very simple:

`   python keepcool.py`



