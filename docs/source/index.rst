.. library documentation master file, created by
   sphinx-quickstart on Mon Mar  4 14:00:55 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to library's documentation!
===================================

.. Contents:

.. toctree::
   :maxdepth: 2


What is this all about?
+++++++++++++++++++++++

This is a Django site, which tries to implement a p2p phisical library.
The current implementation is a bit to traditional.

Do you want to contact us?
++++++++++++++++++++++++++

Please write a mail to brodul [at] kiberpipa [dot] org.

Or find us on IRC channel #kiberpipa on irc.sioff.net server.

Code, issue tracker
+++++++++++++++++++

Code and issue tracker are hosted on `gihub <https://github.com/kiberpipa/library>`_.

   - `Code <https://github.com/kiberpipa/library>`_
   - `Issues <https://github.com/kiberpipa/library/issues>`_

Installation
============

You need `git` installed on your system::

    git clone git://github.com/kiberpipa/library.git

    cd library

    ln -s buildout.d/development.cfg buildout.cfg

    python bootstrap.py -v 1.7.0

    bin/buildout

Run::

    bin/django syncdb

To create the database and make a super user::

    bin/django migrate


Load some development data in the database::

    bin/django loaddata liby/books/fixtures/development.json

    bin/django runserver

Open you browser on localhost:8000

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

