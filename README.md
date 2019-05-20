Python-Course repository
========================

In this repository, we offer the material for a Python programming class. The
idea is to offer an example-driven course. The interested student should go
through the examples given in the [examples](examples) directory of this
repository. In there, you will also find another Readme which will guide
you through the examples and give you the correct order.

Authors
-------

* Jens Dede, ComNets Uni Bremen, <jd@comnet.uni-bremen.de>
* Vishnupriya Parimalam, ComNets Uni Bremen, <vp@comnets.uni-bremen.de>

Content
-------

* `examples`: Contains examples for the Python functions covered during the
  class.
* `slides`: Contains the introduction slides for this course.


Installing Python 3
-------------------

This course focusses on **Python 3**. Please ensure that you install the
correction version! The support for Python 2 ends in January 2020, c.f.
https://www.python.org/dev/peps/pep-0373/.

For Linux, Windows, MacOS, Anaconda is a good option to install Python including all dependencies: https://www.anaconda.com

Alternatively, you can also use the classic installation methods:

* Linux: Preferably use the system repository (i.e., `sudo apt install python3`)
* Windows / Mac: https://www.python.org/downloads/

Although one could use arbitrary text editors for programming, we will give a brief introduction to two editors:

* Spyder
* Jupyter Notebook (web-based)

Both are shipped with Anaconda.

Installing Additional Libraries
-------------------------------

You might need additional functionality which is packet into separate
libraries. Depending on your installation method, you can install for example
`matplotlib` -- a library for graphing -- as follows:

* Debian-based Linux distributions like Ubuntu: `sudo apt install python3-matplotlib`
* Anaconda: `conda install matplotlib`
* *Classical* installation: `pip3 install matplotlib`

Links
-----

### Editors

For programming in Python, you need a text editor which is capable to store
plain text files (i.e. not tools as Libreoffice Writer or Microsoft Word). All
major operating systems some with such an editor (Notepad in case of Windows)
but it is worth having a look on more powerful editors like for example:

* Spyder (also shipped with Anaconda): https://www.spyder-ide.org/
* Notepad++ (Windows): https://notepad-plus-plus.org
* Programmers Notepad (Windows): http://www.pnotepad.org/
* Eclipse (all): https://eclipse.org/
* Scite (all): http://www.scintilla.org/SciTE.html
* Visual Studio Code (all): https://code.visualstudio.com/
* Jupyter (also shipped with Anaconda): https://jupyter.org/
* ...


### Tutorials and cheat sheets

The Internet is full of programming tutorials. Here, we list a couple of them:

* Think Python (PDF, Python 2): http://www.greenteapress.com/thinkpython/thinkpython.pdf
* A web-cheatsheet for Python: https://www.pythoncheatsheet.org
* wikibooks (Python 2, Python 3): https://en.wikibooks.org/wiki/Subject:Python_programming_language
* Easy step-by-step tutorial (Python 3): https://likegeeks.com/python-programming-basics/
* Official Python Docs (Python 3): https://docs.python.org/3/
* Official Python Tutorial (Python 3): https://docs.python.org/2/tutorial/
* How to write good idiomatic Python (Python 2, Python 3): https://github.com/JeffPaine/beautiful_idiomatic_python/blob/master/README.md

More experienced tutorials:

* Beginning Game Programming for Teens with Python (Python 2): https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
* Program Arcade Games with Python and Pygame (Python 3): http://programarcadegames.com/

### Online Interpreters

Some online Python interpreters exists. They are ideal for trying out simple
examples. However, for more complex code, they are overextended.

* http://www.pythontutor.com/
* https://wandbox.org/
* https://ideone.com
* http://codepad.org


Not covered in this course (but maybe nice to know)
---------------------------------------------------

* How to write own modules
* Version Control Systems (VCS) like git (github), SVN, Mercurial, ...
* Doxygen Style for proper commenting
* ...

Contribute
----------

Whoever is interested in contributing: Feel free to fork and send pull requests

License
-------

The content of this repository is licensed under GPLv3
