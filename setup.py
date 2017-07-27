##############################################################################
#
# Copyright (c) 2006, 2011 Zope Foundation and Contributors.
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
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.size package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

ZCML_REQUIRES = [
    'zope.component[zcml]',
    'zope.configuration',
    'zope.security[zcml]',
]

TESTS_REQUIRE = ZCML_REQUIRES

setup(name='zope.size',
      version=read('version.txt').strip(),
      url='http://github.com/zopefoundation/zope.size',
      license='ZPL 2.1',
      description=\
          'Interfaces and simple adapter that give the size of an object',
      keywords="size display human bytes",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development',
      ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      tests_require=TESTS_REQUIRE,
      test_suite='zope.size.tests.test_suite',
      extras_require={
          'zcml': ZCML_REQUIRES,
          'test': TESTS_REQUIRE,
      },
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.i18nmessageid',
      ],
      include_package_data=True,
      zip_safe=False,
)
