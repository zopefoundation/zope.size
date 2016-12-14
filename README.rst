``zope.size``
=============

.. image:: https://travis-ci.org/zopefoundation/zope.size.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.size

.. image:: https://readthedocs.org/projects/zopesize/badge/?version=latest
        :target: http://zopesize.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

This package provides a definition of simple interface that allows
applications to retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the ``getSize``
method that returns size in bytes.  However, the adapter won't crash if an
object doesn't have one and will show size as "not available" instead.

Development is hosted at https://github.com/zopefoundation/zope.size
