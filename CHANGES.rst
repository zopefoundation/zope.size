Changes
=======

6.0 (2025-09-12)
----------------

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.1 (2025-02-14)
----------------

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-06-30)
----------------

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.11.


4.4 (2022-08-30)
----------------

- Drop support for Python 3.4.

- Add support for Python 3.8, 3.9, 3.10.


4.3 (2018-10-05)
----------------

- Add support for Python 3.7.


4.2.0 (2017-07-27)
------------------

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6, 3.2 and 3.3.


4.1.0 (2014-12-29)
------------------

- Add support for PyPy3.

- Add support for Python 3.4.

- Add support for testing on Travis.


4.0.1 (2013-03-08)
------------------

- Add Trove classifiers indicating CPython and PyPy support.


4.0.0 (2013-02-13)
------------------

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.

- Add support for Python 3.2 and 3.3.

- Conditionally disable tests that require ``zope.configuration`` and
  ``zope.security``.


3.5.0 (2011-11-29)
------------------

- Include zcml dependencies in configure.zcml, require the necessary packages
  via a zcml extra, added tests for zcml.

3.4.1 (2009-09-10)
------------------

- Add support for bootstrapping on Jython.

- Add docstrings.

- Beautify package's README and include CHANGES into the description.

- Change package's url to PyPI instead of Subversion.

3.4.0 (2006-09-29)
------------------

- First release as a separate egg
