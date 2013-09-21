====================
 Local Task Tracker
====================

This repository contains a small Django app, developed to track tasks
students attending OpenHatch events might work on.

Running
=======

To run the application, first make sure you have a virtualenv_
created::

  $ cd new-mini-tasks
  $ virtualenv .

Then activate_ the virtualenv; this will allow you to install the
dependencies without interfering with other development work you may
be doing.

::

  $ source bin/activate
  (new-mini-tasks)$

The prompt changes to let you know you were successful.

Now you can install the dependencies::

  (new-mini-tasks)$ pip install -r requirements.txt
  Downloading/unpacking Django==1.5.1 (from -r requirements.txt (line 1))
  Downloading Django-1.5.1.tar.gz (8.0MB): 8.0MB downloaded
  Running setup.py egg_info for package Django

    warning: no previously-included files matching '__pycache__' found under directory '*'
    warning: no previously-included files matching '*.py[co]' found under directory '*'
  Installing collected packages: Django
  Running setup.py install for Django
    changing mode of build/scripts-2.7/django-admin.py from 644 to 755

    warning: no previously-included files matching '__pycache__' found under directory '*'
    warning: no previously-included files matching '*.py[co]' found under directory '*'
    changing mode of /home/nathan/p/new-mini-tasks/bin/django-admin.py to 755
  Successfully installed Django
  Cleaning up...

Now you can set up the database::

  (new-mini-tasks)$ python manage.py syncdb --noinput
  Creating tables ...
  Creating table auth_permission
  Creating table auth_group_permissions
  Creating table auth_group
  Creating table auth_user_user_permissions
  Creating table auth_user_groups
  Creating table auth_user
  Creating table django_content_type
  Creating table django_session
  Creating table django_site
  Creating table django_admin_log
  Creating table tasks_task
  Creating table tasks_student
  Installing custom SQL ...
  Installing indexes ...
  Installed 0 object(s) from 0 fixture(s)
  (new-mini-tasks)$

Yay!

Now you can run the application::

  (new-mini-tasks)$ python manage.py runserver
  0 errors found
  Django version 1.5.1, using settings 'minitasks.settings'
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

Visit ``http://127.0.0.1:8000/`` in your browser to see the
application.

Importing Data
==============

You can import a CSV file using the ``importtasks`` manage command::

  (new-mini-tasks)$ python manage.py importtasks data.csv

This assumes the CSV comes from Asheesh's Google Doc. We may want to
improve that at some point. To get that sample data, run::

  wget 'http://linode.openhatch.org/~paulproteus/tmp/tasks/data.csv'



.. _virtualenv: http://www.virtualenv.org/
