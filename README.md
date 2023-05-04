# Django Glossary 

[![Github Build](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/build.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/build.yml)
[![Github Docs](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/Geoluminate/geoluminate-glossary/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/Geoluminate/geoluminate-glossary)
![GitHub](https://img.shields.io/github/license/Geoluminate/geoluminate-glossary)
![GitHub last commit](https://img.shields.io/github/last-commit/Geoluminate/geoluminate-glossary)
![PyPI](https://img.shields.io/pypi/v/geoluminate-glossary)
<!-- [![RTD](https://readthedocs.org/projects/geoluminate-glossary/badge/?version=latest)](https://geoluminate-glossary.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/build-docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-glossary/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/Geoluminate/geoluminate-glossary)](https://github.com/Geoluminate/geoluminate-glossary/pulls)
[![Issues](https://img.shields.io/github/issues-raw/Geoluminate/geoluminate-glossary)](https://github.com/Geoluminate/geoluminate-glossary/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/geoluminate-glossary) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/geoluminate-glossary) -->

A Django application for managing collections of scientific instruments

Documentation
-------------

The full documentation is at https://ssjenny90.github.io/geoluminate-glossary/

Quickstart
----------

Install Django Glossary::

    pip install geoluminate-glossary

Add it to your `INSTALLED_APPS`:


    INSTALLED_APPS = (
        ...
        'glossary',
        ...
    )

Add Django Glossary's URL patterns:

    urlpatterns = [
        ...
        path('', include("glossary.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

