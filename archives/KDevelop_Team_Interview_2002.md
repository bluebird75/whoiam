## Introduction

KDevelop is the well-known IDE attached to the KDE project. You can browse its website : [www.kdevelop.org](http://www.kdevelop.org)

The interview was conducted by email during May 2002.

Interviewer : Bluebird

Hosting and help : Orzel

Help : Benjamin Adler

## Interview

**Bluebird** : How was the project started ?

**F@lk Brettschneider** : AFAIK Sandy Meier founded it. Some people from his university helped him. Ralf Nolden has also been a member from the first days.

**Victor Roeder** : Although it's Sandy's story, I'm telling it now :-) Somewhen 1998 Sandy Meier started KDevelop and worked 8 weeks alone on this project. After 2 or 3 fellow students of him added some features, 0.1 was released on the Sept. 22. 1998. After 0.1 Ralf Nolden joined. 3 months later 0.2 was released. Then Pascal Kramer integrated the dialog editor and Jonas Nordin rewrote the C++ parser for the class browser. Release 0.3 came along. After that 0.4 was released but I don't know what was new in that version. After that 1.0beta1 was released. That was more or less the beginning. On the 4th May of 1999 [www.KDevelop.org](http://www.KDevelop.org) got online the first time!

**Bluebird** : Who is working on KDevelop ?

**F@lk Brettschneider** : You'll find this information in the KDevelop About box and on the website. The current core team is : <http://www.KDevelop.org/index.html?filename=current_work.html> . Additionally, we got hundreds of patches the year from people all over the world. See : <http://www.KDevelop.org/index.html?filename=authors.html>

**Bluebird** : Who are you and how did you start contribute to the project ?

**F@lk Brettschneider** : I became a user of KDevelop on version 0.4 or about that time, around summer 1999. It was pretty close to MSVC that I was used to. First I was just a bugger and bothered the list with nice bug reports, especially for the integrated debugger patch of John Birch which was the coolest piece of source code I've seen on Linux until that day.

Later I send small patches and helped Sandy Meier with the first attempt of integrating MDI in KDevelop. After that I implemented MDI by myself from scratch for KDevelop-2.0 one year ago. That time I've learned how KDevelop works. The last year I've spent with fixing various bugs. Now the result of our work is an upcoming pretty cool KDevelop-2.1.1 that I love to use as my favourite IDE at my daily work.

I think the important thing is that you must always be a KDevelop user. For instance when it crashes 3 times the week with the same backtrace, you'll get mad about it and will fix it as soon as you find the time. That's my secret recipe. :)

**Per Edin** : I live in the little city Norrk�ping in Sweden. I have been a Windows programmer (C++) since late 98 and a Linux programmer (C++) since about the same time.

I started to use KDevelop at version 1.4, around may 2000. I was very new to Linux GUI programming. And as F@lk, I recognized a lot of MSVC. I just started to help the development of it by trying to implement multiply projects and workspace support in KDevelop, which is going smoothly.

**Roberto Raggi** : I became a KDevelop developer in feb 2002. I've ported/extended the code completion stuff from Gideon to KDevelop 2.1. After that, I added a modified version of qt-designer editor to Gideon, code template and parts support to KDevelop2.2. Now i'm trying to implement C# and OCaml support for Gideon.

**Daniel Engelschalt** : I'm living in Dresden / Germany. With Victor Roeder, I have implemented the first version of code completion and worked on the class store. We are currently reorganizing code completion stuff.

I wanted to learn Qt - and KDevelop was the IDE to start. I looked into the bugs file, picked the first I saw and tried to fix it! This was around 2001

**Victor Roeder** : I'm student of Computer Sciences in Business Administration in Furtwangen (black forest), Germany. In 1999 I wrote a mail to Sandy because of an idea I had for KDE development. He told me to do it by myself :-) and I started [www.ksourcerer.org](http://www.ksourcerer.org) together with a friend of mine AND Burkhard Lehner, the famous author of the book "KDE- und Qt-Programmierung" (but that's not really important, because this site is not online any more :-).

At the german "Linux Tag" 2001, I met Bernd Gehrmann and Sandy and we talked about Gideon. I was impressed so that I got involved (with the many help of Sandy :-). But my "code output" was not really huge :-). For Gideon: I started with C++ code completion but that was not really great, I assist in adding persistant functionality to the existing class store so that projects are loaded faster. Now I'm working on the autoprojectpart of Gideon (see <http://www.kdevelop.org/index.html?filename=current_work.html> for details).

**John Birch** : I started on KDevelop 0.4 by producing a patch to add the debugger. 0.4 hung around for what seemed like ages before 1.0 came out, still without my debugger, as everyone wanted a stable KDevelop. (My patch was too invasive to go into a stable release). For 0.4 , I helped with some bug fixes, particularly working with Walter and Sandy, which was great fun.

Once 1.0 came out I added the debugger code to KDevelop and we released KDevelop1.1 .

Somewhere just before 1.0, there was this annoying guy telling me I had bugs in the debugger and why doesn't it do this and that. The result was :

- a better debugger
- F@lk Brettschneider joined KDevelop :-)

Currently I'm not contributing much due to work commitments, only just able to keep track of what is happening. I'll like to do a lot more that this but...

Some time in the future I'd like to see a KDevelop development meeting in Europe, so I can meet a lot of the other developers. Maybe based around one of the linux shows where KDE has a booth, (although we could have our meeting in the pub down the road :-)

**Walter Tasin** : My name is Walter Tasin and I'm working in the Munich University of Applied Sciences/Dept. Electrical Engineering and Information Technology (since 1991). Apart from working I've begun last year to study again to give my actual degree an international name ;-).

Location : nearby Munich, Germany Nationality : Italian

In May 1999 the Dept, I was given the task to look for an easy to use IDE for programming linux console apps. So surfin' around I found KDevelop, which looked very promising to me. I began to write patches for KDevelop 0.4 to solve some crashes. Since KDevelop 1.0 I'm official member of the KDevelop team. general task description : bugfixing, general enhancements in usability, if I find the time I also take care of console-projects, autoconf/automake-stuff inside KDevelop, etc. ...

**Sandy Meier** : I am the original author, who implemented the first "framework". I was the maintainer until KDevelop 1.3. Then I reduced my input to the project and write only some codelines for Gideon/KDevelop now.

I work currently on the Gideon/KDevelop version, mainly to add PHP and GBA (Gameboy Adv. :-)) support. Gideon is a complete new IDE initial written by Bernd Gehrmann.

**Bernd Gehrmann** : My first encounter with KDevelop was at the beginning of 1999. Before that time, the most "visible" KDE based IDE was KodeKnight. It was based on MICO and therefore needed 128 MB RAM to compile, so on my computer a full build needed half a day. KDevelop was a lot more modest, and it was very polished even in the early versions, with tooltips and what's this help anywhere. As it looked very promising, I sent a mail with a long list of ideas. After some weeks, it turned out that nobody was going to implement all my suggestions, so I had to do it myself ;-)

**Roland Krause** : I have implemented and now maintains ctags support in KDevelop-2.

I was looking for an IDE for a project at work, tried both KDEStudio and KDevelop and decided on KDevelop because the development team was immediately responsive. I started using KDevelop for everyday work in January 2001.

**Eray Ozkural** : I'm a PhD student at Comp. Sci. Dept. at Bilkent University, Ankara. My research interests are data mining, parallel programming and AI in general. I started using KDE regularly after the incredible 2.2 release.

I've began contributing to KDevelop about 6 months ago. I added debian packaging for Gideon branch (HEAD) and then I fixed a few small bugs. I also added some features to KDevelop 2 editor and fixed a few trivial bugs, code which was last replaced by the new editor IIRC. :)

As a result I'm now using mostly xemacs ;)

My current Gideon project is a part that will enable navigation of code. For that I have been planning to use source navigator but it's a little more complicated than it seems. I will join in the new sourcenav development at sourceforge. For this to work, however, one will have to make sure that the implementation of the source database is transparent to end users, a problem on which I have not worked on yet. Ahem. Right now, most of my volunteer time is going to a berkeley DB front end that I am working on. I plan to use this code in both noatun and Gideon. (Now that sounds cyberpunk)

Another project that I have in mind would be integration of new editors to Gideon. I've determined a few interesting targets to that end.

Richard Dale : I'm was a longtime Objective-C/NeXTSTEP developer before I got into Qt/KDE programming. I'll try and describe my view of the (complex) history of the project since late 1999..

I was trying to port Squeak Smalltalk to GNUstep in September 1999, and couldn't find a Linux text editor or IDE that supported Objective-C. KDevelop looked promising, but crashed when I tried to edit some Objective-C. So I fixed the crash by making parse Objective-C - not as hard as it sounds because it is actually a pretty simple language.

I carried on adding syntax highlighing and so, and was most suprised to find that after a week or so I had a perfectly usable Objective-C IDE. I built a patch and Sandy Meier put it on the KDevelop site. I gave up the Squeak work, when I found it was more fun to try and produce a complete KDE Objective-C programming environment with Qt/KDE language bindings.

At that time (early 2000), the development plan for KDevelop was that version 1.x would be targeted at C/C++ developers, and version 2.x would support multiple languages. So while I waited for KDevelop 2.x to be ready, I carried on doing Objective-C bindings, which took much more work than I expected. But by September 2000 I finally had the bindings problem cracked and started doing Java bindings too.

I waited a long time, until December 2000, before I could add Java and Objective-C support to the complex and flaky 2.x app. But it wasn't usable, and it was only when Bernd Gehrmann came up with the Gideon rewrite in about April 2001, that I could port my parsers and manage to edit Java or Objective-C without the app crashing. Meanwhile, KDevelop 1.x had got so much developer attention and improvements that it was renamed KDevelop 2.x, and Gideon was to become KDevelop 3.0.

The java support in Gideon is especially interesting, in that it is the only C++ IDE that allows you to write KPart based plugins in Java. Bernd had to strip out MDI support from Gideon in order to get something stable, that developers could work on. But this was regarded as such an essential feature, that some KDevelop 2.x developers were very reluctant to switch to Gideon. So work on the two IDEs has continued in parallel. Only recently have attempts be made to 'synergise' developments by allowing common KParts to be used by both IDEs.

**Harald Fernengel** : I'm studying computer science for 3 and a half years now and will hopefully finish this summer.

I was looking for a good IDE and KDevelop was the most mature one. I found some usability thingies in KDevelop pre-2.0 and fixed them. As so often with open source, the guys who do the work do the decisions so I became a part of the KDevelop team.

I'm investing about 4-10 hours per week for KDE/KDevelop and do wherever I see the need for improvements, which is mostly bug-fixing and usability improvements.

**Bluebird** : Do you use KDevelop in your everyday project ?

**Roland Krause** : Yes, I use use KDevelop at work every day. I maintain a linear algebra library with it.

**F@lk Brettschneider** : Of course. I'm used to MSVC. After switching to Linux I had to work with XEmacs and DDD and that was absolutely horror. Even in my early years, I used vi and joe and command line make. I also tried KDEStudio and some other IDEs including KDbg but I was just satisfied when I discovered KDevelop with its integrated debugger.

**Per Edin** : Of course! I really like the UI because it looks almost the same as MSVC.

**Bluebird** : Could you clarify the situation on KDevelop and Gideon ?

**Roland Krause** : Ok, this is what happened. There was a dispute on the mailing list as to the future of KDevelop. Basically some people wanted to keep the old codebase, some people didnt.

A new codebase, created by Bernd, was put into CVS HEAD. It's working name is "Gideon".

Maintenance was performed on a branch called KDE_2_2_BRANCH. This was the version that was released with KDE-2.x. The maintenance version began a life of it's own.

So another branch was created in which the internal kwrite editor was removed and replaced by a kate part. This branch was KDEVELOP2BRANCH. The only person which ever worked on it was me until Robe started hacking on it too. The project isnt finished but it worked.

We then put this branch back into HEAD and it is now more or less maintained parallel to Gideon.

The reason for two applications are that a few people, one of them me, dont believe in rewriting applications and that some people want a MDI based user interface.

Currently there is not much work being done on KDevelop in HEAD but most people turned out to be hacking on Gideon, which now also has an MDI interface although I havent tried it. I expect one version to go away in the long future.

**Bluebird** : My god. So we have three branches. KDevelop 2, KDE 2 and Gideon ?

**F@lk Brettschneider** : KDE_2_2_BRANCH is locked for further development. Only bugfixes for crashes are allowed to commit after a strong review procedure. We release the current 3 or 4 (but important) bugfixes as KDevelop-2.1.1 bundled in the KDE-3.0.1 release.

KDEVELOP_2_BRANCH was buried 3 weeks ago. It has moved to cvs HEAD in parallel to Gideon. So HEAD is containing the future versions, although there are 2 candidates at present.

**Bluebird** : Which branch is part of the official KDE 3 release ?

**F@lk Brettschneider** : Actually, KDevelop-2.1 is a new version for KDE-2. That's why it comes from the KDE_2_2_BRANCH. But we just changed about 30 lines and suddenly it also compiled and ran on KDE-3. So it was released as our new KDE-3 version. Just Walter Tasin put additional effort in adapting the project templates to templates working on both KDE versions.

**Bluebird** : So, to be sure I get this straight:

- KDE_2_2_BRANCH is the version originating from the KDevelop 2.0 release (15 august), which was release along with KDE 2.2 . This is a stable branch, for bugfixing only. This branch is also the one leading to KDevelop 2.1, released on april, 4th.
- KDEVELOP_2_BRANCH is a branch with new features originating from KDE_2_2_BRANCH. When was this branch created ?

**F@lk** : Right, it was branched from KDE_2_2_BRANCH by Roland Krause on 8th August 2001.

**Bluebird** : And Gideon is a complete rewrite.

**Bernd** : No, it's KDevelop minus the bad code plus more good code ;-) (where in many cases "bad" means "C++ specific" or "automake specific" or "specific for a compiled language")

With Gideon, you can (or will be able to) develop PHP, Python, Perl or Java programs. Comparing it to KDevelop is like comparing apples with oranges. KDevelop simply doesn't play in the same league as Gideon.

**Bluebird** : Do you think Gideon was a good concept or a bad idea, and why ? If Gideon is so different/new, how can it be possible that its kpart might be reusable in standard KDevelop ? I don't want to start a flamewar though!

**Victor** : I think Gideon has a very well designed and matured structure. And that's from the beginning :-). It's written like an IDE (or an application in general) has to be written. What's missing are 15-20 developers ;-) ...

**Bernd** : To answer your question, the claim that KDevelop might use Gideon KPart is probably a cheap marketing gag ;-)

Gideon's structure is really very different from KDevelop. It is designed for extensibility to the core, i.e. almost all core functionality is provided by plugins, and consequently plugins can use the same interfaces to other components as any core component. That's why the interaction between components must follow a very different model than in a monolithic application. To give you two examples :

What happens if you right-click on a tree view in KDevelop? The tree view will insert some items into the context menu. If the user chooses one of them, the tree view invokes the corresponding function in the correct component. In other words, KDevelop uses a push model. A tree view must know each component that is responsible for context menu items. It is clear that such a model does not allow for plugins to extend the context menu. In contrast, Gideon follows a pull model. When the user opens the context menu, the tree view shouts "Listen everybody! The user has clicked on a file". All plugins offering file-related functionality listen to such a message and insert their items into the context menu. You see that the tree view in which the context menu has been opened doesn't have to know anything about other plugins.

This difference in design is not only important for extensibility, it also has a big practical advantage. Experience with developing KDevelop shows that the bottleneck for the communication between different subsystems of the IDE lies in one class. Every time you change even a small thing, you have to recompile all files that include the header file that defines this class. In the times of KDevelop 1.0betaX, this frequently led to compilations of half an hour, which was totally frustrating. In Gideon, mere changes of some implementation never require the compilation of files outside of the affected plugin. You only have big recompiles when an interface changes, and that is relatively rare.

Another example are the language specific features. In KDevelop, whenever the IDE thinks that the language parser should be invoked, it calls the appropriate function. In Gideon, this is impossible, because the language support part of the used language decides itself when it starts to parse. And in fact, this is done in different ways for different languages : C++ is only parsed when a file is saved, as the parser is relatively slow (with increasing processor speed, this may change sometime). PHP has a realtime parser, i.e. is updates each time the user modifies a file. Docbook has a "delayed-realtime" parser, i.e. it starts to parse when the editor is idle for a second or so.

**Bluebird** : For what platforms can you use KDevelop ? With which toolkit ?

**Roland Krause** : I have used it on Linux, Solaris SPARC and SOLARIS X86. I have used it with Qt and proprietary toolkits. You can use KDevelop to develop with all known toolkits that make sense and are available from compiled languages (C,C++,Fortran). Gideon allows you to develop in scripting languages Python Perl, Java, you name it.

**Bluebird** : Can you develop libraries as well as application ?

**Roland Krause** : Yes, but there are some gotchas in the current stable version, the development version is going to have more flexibility here.

**Bluebird** : Could KDevelop be used for KDE ? I mean, could we create a KDevelop project file to handle KDElibs for example ?

**Roland Krause** : Yes, and in fact it should, any project where the developers dont use the tools they develop is ulimately doomed to fail.

**Bluebird** : Do you have code completion ?

**Roland Krause** : Yes. Works in a failry restricted manner currently but it will improve.

**Bluebird** : there is a kapptemplate generator in KDEsdk, do you use that ?

**Roland Krause** : No, but we should probably.

**Bluebird** : Is KDevelop's template generator usable separetely from KDevelop ?

**Roland Krause** : Yes.

**Bluebird** : So how about merging the two ?

**Roland Krause** : Very good idea! Go right ahead :-) aehem...

**Bluebird** : Can you generate .pro files, for qmake/tmake based projects ?

**Roland Krause** : Yes, Gideon has a plugin that can at least read .pro files.

**Bluebird** : Is it possible to use KDevelop as a source browser ?

**Roland Krause** : Yes. This works very well, install exuberant ctags then generate and load a tags file and you can quickly jump to declarations and definitions. (Shameless plug, he he)

**Bluebird** : Is it easy to import an existing project into KDevelop ?

**Roland Krause** : That depends, the closer it is to the standard automake autoconf structure the better it is. In Gideon it is very easy to import all kinds of projects.

**Bluebird** : Have you had support from other toolkits, projects or people to help KDevelop ?

**Roland Krause** : No. This is a KDE project. Lot's of people have contributed small things and some people have contributed a lot.

**Bluebird** : Is it possible to generate a project with KDevelop and work on it manually after that ? Do the Makefile.am look good ?

**Roland Krause** : Yes, it is possible. The other answers depends on what you define as looking good. Speaking of KDevelop there are two ways of doing things :

- Have your project generated by KDevelop, then have it managed by KDevelop and dont touch the Makefile.am, at least no excessive changes.
- Manage it yourself, then do whatever your heart desires. Mixed management doesnt work well in KDevelop. This has changes dramatically with Gideon's much better project manager.

**Bernd** : Initially, KDevelop was not meant to support more than single-binary projects for a single developer. IMO is does an excellent job in providing a simple user interface for such projects, and in particular using automake as backend is an innovative approach, if you compare with other IDEs that force you into their proprietary build system.

Of course, it has grown out of these bounds, that's why a more powerful and less intrusive handling of Makefile.ams has been on the TODO list for a long time. Gideon can write and read Makefile.ams and modifies only the changed lines. So even if multiple developers work on the same project simultaneously, it is relatively easy to resolve conflicts etc.

The problem here is that it is very difficult to make all the flexibility of the underlying build system available through a nice user interface (i.e. to make all-day usage simple, while making more advanced things possible), and feedback from users will surely be helpful. Also it isn't really helpful that KDE developers invent their own build system am_edit, which is incompatible with vanilla automake semantics, a moving target, and moreover totally undocumented.

**Bluebird** : How much do you integrate with Cervisia, KDbg, QtDesigner, kdiff, ... ?

**Bernd** : You can add a lot of tools into the Tools menu. This is more flexible than it looks it first glance, e.g. you can insert certain placeholders in the command line which get replaced with the project directory, current file etc. Integrating Cervisia better is a matter of making it more modular, so that not the whole user interface has to be swallowed. KDbg... well, has it anything that the integrated debugger hasn't? You can add Qt designer files to a project, but for editing dialogs you invoke designer as external process with a separate main window. As designer is practically an IDE for itself (in particular if you look at BlackAdder or QSA which are based on it), it would require a huge effort to achieve a tighter integration.

**Bluebird** : How about bitkeeper (and other cvs-thingies) support?

**Bernd** : In Gideon, such things can easily be provided as plugins. IMO, it would be natural if the companies behind such tools funded the development of appropriate plugins. Support for Subversion would be cool too. Volunteers are welcome :-) It's really easy, if you look at the cvs part.

**Bluebird** : What editors are available with KDevelop ? any plan for future ?

**Bernd** : The released versions still have a quite old version of kwrite. Gideon uses the KTextEditor interface in kdelibs, so you can use any editor that implements this interface. Currently available are kate, qeditor (based on the editor in Qt designer) and nedit. Naturally, you will not get the same amount of integration with all of them. Our main interest is of course in those which provide the features an IDE needs, like a code completion box. Nevertheless, people who implement other editors are welcome to ask if they have problems.

**F@lk Brettschneider** : Well, I know many of the KDE hackers avoid KDevelop because they miss the Emacs editor. We've got the KWrite, Kate, NEdit and QEditor integration in Gideon but the actual killer feature would be the Emacs integration. Unfortunately, we haven't found someone able and willing to implement that interface. **Bluebird**, maybe you can do some advertisment for that job. ;-)

**Harald Fernengel** : Don't forget kvim, it is already a KPart and a KTextEditor interface is on its way. There are a few problems with the focus but besides that it runs just fine in Gideon.

**Bluebird** : I was afraid nobody was aware of it! I am one of the author of KVim, and especially of the Vim KPart. Our goal has always been Vim inside KDevelop. Now Mickael Marchand is doing all the work and it is getting really really good. See the the KVIM homepage (on this very same site) and the KDE extragear cvs module. </shameless publicity>

**Bluebird** : What other tools/plugin does KDevelop integrate ?

**Bernd** : Hmm, kdoc, konsole, ctags, cvs and grep come to mind. Gideon also integrates doxywizard, ftnchek, Artistic Style and a Gameboy Advance simulator.

**Bluebird** : PF: What languages can currently be used with KDevelop ? Future plans ? .NET / C# - support? (would that make sense in any way?)

**F@lk Brettschneider** : C/C++ only with KDevelop-2.x. More languagues with KDevelop-3 aka Gideon.

**Roberto Raggi** : At the moment Gideon supports C++, Java, Python, Perl, Php and fortran.. but add support for a new language is very simple. Now i'm trying to add it for C# and OCaml.

**Bluebird** : When are the next releases expected (each branch) ?

**F@lk Brettschneider** : The next release is KDevelop-2.1.2 bundled with KDE-3.0.2. I don't know what comes next with KDE-3.1. Maybe KDevelop-3.0 aka Gideon is usuable until then.

**Bluebird** : What do you plan ? Do you want a release separated from KDE ?

**F@lk Brettschneider** : No. Bundling to KDE is cool. There's no need to do packaging and promoting jobs for us, we just code and code and code.

**Bluebird** : How about releasing a windows-version sometimes?

**F@lk Brettschneider** : I'd second that. It's very interesting for all the commercial Qt-programmiers using KDevelop for cross-platform development. It would be an alternative to MSVC or Borland Builder also on Win32.

**Bluebird** : What do you plan for the long term ?

**Eray** : Sourcenav source code navigation database. Something that would replace the persistent class store basically (and hopefully in a better way). Right now I'm working on making kvim part good enough for Gideon ;) I might commit some stuff in near future.

**Bluebird** : Where do you need help ?

**Eray** : With sourcenav. Devels should join sourcenav devel team at the sourcenavigator site if they're interested. There's a new release right now, but we need to factor out some essential components if we want to use it for Gideon.

**Bluebird** : Where would you like to see people contributing ?

**Eray** :

- mainly KDevelop 3.0 We need to get an alpha release out.
- cleaning up the code, fixing bugs, have a look at TODO file :)
- integrating better/advanced editors

**F@lk Brettschneider** : I'm really interested in the 2 killer features KDevelop-2.1 is missing. It's the Workspace(.dsw)<->Project(.dsp) approach of MS Visual C++ to get the MSVC fans to KDevelop, and Emacs integration to get the ancient hardcore KDE gurus to KDevelop. :-) Vim integration will show how easy it is to embed non-Qt stuff in KDevelop...

**Bluebird** : Thank to all of you for working on KDevelop and doing this interview.