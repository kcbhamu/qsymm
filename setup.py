#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys


if sys.version_info < (3, 5):
    print('Qsymm requires Python 3.5 or above.')
    sys.exit(1)


install_requires = [
    'numpy>=1.13',  # because we use __array_ufunc__
    'scipy',
    'sympy',
    'tinyarray',
    'notebook',
]

extras_require = {
    'kwant': ['kwant'],
}


setup(
    name='qsymm',
    description='Symmetry finder and symmetric Hamiltonian generator',
    version='1.0.0',
    url='https://gitlab.kwant-project.org/qt/qsymm',
    author='Qsymm authors',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages('.'),
    install_requires=install_requires,
    extras_require=extras_require,
)