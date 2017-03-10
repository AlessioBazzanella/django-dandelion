.. _Dandelion: https://dandelion.eu

Welcome to Django Dandelion's documentation!
============================================

Use the Dandelion_ API with Django

Installation
------------

``django-dandelion`` is available on :samp:`https://pypi.python.org/pypi/django-dandelion/` install it simply with:

.. code-block:: bash

    $ pip install django-dandelion

Add the entry DANDELION_TOKEN. The recommended method is to setup your production keys using environment
variables. This helps to keep them more secure. Your test keys can be displayed in your code directly.

The following entry look for your DANDELION_TOKEN in your environment and, if it can’t find them,uses your test keys
values instead:

.. code-block:: python

    DANDELION_TOKEN = os.environ.get("DANDELION_TOKEN", "<your dandelion token>")

Contents
--------

.. toctree::
   :maxdepth: 2

   readme
   usage
   contributing
   authors
   changelog
