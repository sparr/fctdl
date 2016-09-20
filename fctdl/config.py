# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import yaml, os
from simple_model import Model, Attribute

def parse_branch(string):
    if string not in ['stable', 'experimental']:
        raise ValueError('no such branch: %s' % string)
    return string

class Config(Model):
    username = Attribute(str, optional=True)
    password = Attribute(str, optional=True)
    branch   = Attribute(parse_branch, optional=True)

def read_config(path):
    if not os.path.isfile(path): return Config()
    with open(path, 'r') as stream:
        content = yaml.safe_load(stream)
    return Config(**content)


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
