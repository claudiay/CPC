#/usr/bin/env python
from distutils.core import setup, Extension
module = Extension('compareplants',
                    sources = ['compare_plants.c'])

setup ( name = 'compareplants',
        version = '1.0',
        description = 'Does the math stuff for CPC.',
        ext_modules = [module])

