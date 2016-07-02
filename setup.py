#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import os, pip

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), 'r').read()

install_reqs = pip.req.parse_requirements('requirements.txt', session=pip.download.PipSession())

requirements = [str(ir.req) for ir in install_reqs if ir is not None]

from fctdl import __version__

setup(name             = 'fctdl',
      author           = 'Aljosha Friemann',
      author_email     = 'aljosha.friemann@gmail.com',
      description      = 'Download factorio alpha from your command line',
      url              = 'https://github.com/afriemann/fctdl',
      keywords         = ['factorio', 'cli', 'games', 'utility'],
      classifiers      = [],
      version          = __version__,
      license          = read('LICENSE.txt'),
      long_description = read('README.rst'),
      install_requires = requirements,
      packages         = [ 'fctdl' ],
      entry_points     = { 'console_scripts': ['fctdl=fctdl.cli:main'] },
      platforms        = 'linux'
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
