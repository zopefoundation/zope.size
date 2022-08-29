===============
 ``zope.size``
===============

.. image:: https://img.shields.io/pypi/v/zope.size.svg
        :target: https://pypi.python.org/pypi/zope.size/
        :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.size.svg
        :target: https://pypi.org/project/zope.size/
        :alt: Supported Python versions

.. image:: https://github.com/zopefoundation/zope.size/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/zope.size/actions/workflows/tests.yml

.. image:: https://readthedocs.org/projects/zopesize/badge/?version=latest
        :target: https://zopesize.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.size/badge.svg?branch=master
        :target: https://coveralls.io/github/zopefoundation/zope.size?branch=master

This package provides a definition of simple interface that allows
applications to retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the ``getSize``
method that returns size in bytes.  However, the adapter won't crash if an
object doesn't have one and will show size as "not available" instead.

Development is hosted at https://github.com/zopefoundation/zope.size

Documentation is hosted at https://zopesize.readthedocs.io
