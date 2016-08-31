#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import logging

from .cli import main

if __name__ == '__main__':
    try:
        exit(main())
    except Exception as e:
        logging.error(e)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
