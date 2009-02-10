##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.size package

$Id$
"""

import os

from setuptools import setup, find_packages

setup(name='zope.size',
      version = '3.4.1dev',
      url='http://pypi.python.org/pypi/zope.size',
      license='ZPL 2.1',
      description='Zope size',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      long_description="Interfaces and adapters that give the size of an object.",

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope'],
      tests_require = [],
      install_requires=['setuptools',
                        'zope.interface',
                        'zope.i18nmessageid'],
      include_package_data = True,
      zip_safe = False,
      )
