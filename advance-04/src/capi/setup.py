#! /usr/bin/env python

from setuptools import setup, Extension

def main():
    setup(name="cutils",
          version="1.0.0",
          description="Example of C-extension",
          author="Anton Kukhtichev",
          ext_modules=[Extension("cutils", ["cutils.c"])])

if __name__ == "__main__":
    main()
