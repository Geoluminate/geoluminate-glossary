=====
Usage
=====

To use Django Glossary in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'glossary.apps.GlossaryConfig',
        ...
    )

Add Django Glossary's URL patterns:

.. code-block:: python

    from glossary import urls as glossary_urls


    urlpatterns = [
        ...
        url(r'^', include(glossary_urls)),
        ...
    ]
