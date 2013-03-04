Installation
============

You need `git` installed on your system::

    ``git clone git://github.com/kiberpipa/library.git``

    ``cd library``

    ``ln -s buildout.d/development.cfg buildout.cfg``

    ``python bootstrap.py -v 1.7.0``

    ``bin/buildout``

Run::

    ``bin/django syncdb``

To create the database and make a super user::

    ``bin/django migrate``


Load some development data in the database::

    ``bin/django loaddata liby/books/fixtures/development.json``

    ``bin/django runserver``

Open you browser on localhost:8000
