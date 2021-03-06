#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from dehumanizer import version

setuptools.setup(
    name="dehumanizer",
    version=version.__version__,
    url="https://github.com/samstudio8/dehumanizer",

    description="A command line tool for rapidly ridding reads of horrid humans",
    long_description="",

    author="Sam Nicholls",
    author_email="sam@samnicholls.net",

    maintainer="Sam Nicholls",
    maintainer_email="sam@samnicholls.net",

    packages=setuptools.find_packages(),
    include_package_data=True,

    install_requires=[
        "mappy",
        "numpy",
        "pysam",
    ],

    entry_points = {
        "console_scripts": [
            "dehumanize=dehumanizer.dehumanizer:cli",
            "dehumanise=dehumanizer.dehumanizer:cli",
        ]
    },

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
    ],

)
