#! /usr/bin/env python

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(['cyutils.pyx'])
)
