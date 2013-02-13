Installation
============

You need `git` installed on your system.

``git clone git://github.com/kiberpipa/library.git``

``cd library``

``python bootstrap.py -v 1.7.0``

``bin/buildout``

``bin/django runserver``

Run:

``bin/django syncdb``

to create the database and make a super user.

Open you browser on localhost:8000
