Python example files
====================

About this directory
--------------------

The idea of this course is to be programming-driven. We offer a set of example
programs using the basic functions of Python. Interested people should go through
them and try to understand by themself. The links to the corresponding
documentation is given in the header of each individual example file. The main Python
documentation is online available under
[docs.python.org](https://docs.python.org/2.7).

For the example which require data, the corresponding [example data files](files) are given in the [files](files) directory.

How to start?
-------------

Go through the example files given in the next section and try to understand
them. The complexity is increasing with each step. After going through all of
these files, you should be able to write a Python script for plotting data with
the following capabilities:

- A command line interface where the input filename and some other options
  like title can be defined
- The Data is read and parsed from the given file. Maybe some further analysis
  is done
- The results should be exported so they can be used for further documentation
  (i.e., in a report)

Things to implement
-------------------

Some ideas what you could implement for further understanding of the language:

* Hello world example
* Print a square / triangle
* Enter name and gender to formulate a greeting
* Print prime numbers
* Try out the random number generators
* Calculate some statistics from user-given numbers
* Create a simple phone book
* Plot a sine / cosine using matplotlib
* Read data from the files directory and plot statistics
* ...


Commented example files
-----------------------

The examples are sorted in an increasing order, i.e., they are getting more
complex. If you are new to Python, you should start at the beginning and go
through all examples step by step. If you are a more experienced programmer,
you can use these examples to lookup how to use certain functions.

1. [helloworldExample.py](helloworldExample.py)
1. [numberExample.py](numberExample.py)
1. [conditionsExample.py](conditionsExample.py)
1. [stringExample.py](stringExample.py)
1. [textInputExample.py](textInputExample.py)
1. [datastructuresExample.py](datastructuresExample.py)
1. [loopsExample.py](loopsExample.py)
1. [castingExample.py](castingExample.py)
1. [functionExample.py](functionExample.py)
1. [datetimeExample.py](datetimeExample.py)
1. [randomExample.py](randomExample.py)
1. [numpyExample.py](numpyExample.py)
1. [classExample.py](classExample.py), [myClassExample.py](myClassExample.py)
1. [csvExample.py](csvExample.py)
1. [argumentParserExample.py](argumentParserExample.py)
1. [matplotlibExample.py](matplotlibExample.py)
1. [pickleExample.py](pickleExample.py)
1. [jsonExample.py](jsonExample.py)
1. [regularExpressionExample.py](regularExpressionExample.py)
1. [exceptionsExample.py](exceptionsExample.py)


FAQ
===

This section contains the frequently asked questions

Package cannot be found
-----------------------

Depending on your Python installation, you might get an error message
complaining that a package is missing like for example the numpy package. You
can install most packages using the pip tool.

* On Unix / Linux / MacOS, you can usually use `pip install <package name>` to
  install packages
* On Windows, you will find the corresponding command in the
  `C:\Python2x\Scripts` directory. Open a shell, cd into that directory and
  execute the command as mentioned above

For this tutorial, the following packages are required:

* `pip install numpy`
* `pip install python-dateutil`
* `pip install matplotlib`

I got an *IndentationError*
---------------------------

Maybe you are mixing space an tabs. According to the documentation
(https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces), you should stick to
spaces. It is also a good idea to setup you text editor to highlight tabs and
replace tabs by spaces (preferable 4 spaces).
