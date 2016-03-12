#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import setuptools_extras

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open('test-requirements.txt') as requirements:
    test_required = requirements.read().splitlines()

if __name__ == "__main__":
    setup(name='setuptools-extras',
          version=setuptools_extras.__version__,
          description=('Extra tools to use with setuptools to handle other '
                       'package managers.'),
          author="AbdealiJK",
          author_email='abdealikothari@gmail.com',
          url='https://github.com/AbdealiJK/setuptools_extras',
          platforms='any',
          packages=find_packages(exclude=["build.*", "*.tests", "tests"]),
          install_requires=required,
          tests_require=test_required,
          license="MIT",
          package_data={'setuptools_extras': ["VERSION"]},
          # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Environment :: MacOS X',
              'Environment :: Win32 (MS Windows)',
              'Intended Audience :: Developers',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: Implementation :: CPython'])
