#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='setuptools-wotmod',
    version='0.2',
    packages=find_packages(),
    description='setuptools integration for creating World of Tanks mods',
    long_description=open('README.md').read(),
    author='jhakonen',
    url='https://github.com/jhakonen/setuptools-wotmod/',
    license='MIT License',
    setup_requires=['pytest-runner'],
    tests_require=[
        'mock',
        'nose',
        'pytest<5',
    ],
    entry_points={
        "distutils.commands": [
            "bdist_wotmod = setuptools_wotmod.bdist_wotmod:bdist_wotmod",
        ],
    },
)
