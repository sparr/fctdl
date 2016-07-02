#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import click, logging, platform

from . import __version__
from .factorio import Factorio

logger = logging.getLogger(__name__)

@click.command()
@click.version_option(version=__version__)
@click.option('--debug/--no-debug', default=False)
@click.option('-u', '--username', prompt='username')
@click.option('-p', '--password', prompt='password', hide_input=True)
@click.option('-a', '--architecture', type=click.Choice(['x86', 'x64']), default='x64' if '64' in platform.machine() else 'x86')
@click.argument('versions', nargs=-1)
@click.argument('path', type=click.Path(exists=True, file_okay=False, writable=True))
def main(debug, username, password, architecture, versions, path):
    """main"""
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    logging.getLogger('requests').setLevel(logging.DEBUG if debug else logging.WARNING)

    try:
        f = Factorio(username, password)
        for version in versions:
            f.download(version, architecture, path)
    except Exception as e:
        if debug:
            logger.exception(e)
        else:
            logger.error(e)
        return 1
    return 0

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
