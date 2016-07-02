#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import requests, os, logging

logger = logging.getLogger(__name__)

download_url = {
    'x86': 'https://www.factorio.com/get-download/%s/alpha/linux32',
    'x64': 'https://www.factorio.com/get-download/%s/alpha/linux64'
}

class Factorio:
    def __init__(self, username, password):
        self._session = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        logger.info('logging in.')
        self._session.post('https://www.factorio.com/login', params = {'username-or-email': username, 'password': password})

    def download(self, version, arch, path):
        logger.info('requesting binary location.')
        response = self._session.get(download_url.get(arch) % version, allow_redirects=False)

        if not response.status_code == 302:
            raise Exception('location request failed: %s' % response.text)
        elif 'Location' not in response.headers:
            raise Exception('No location received in headers: %s' % response.headers)

        binary_location = response.headers.get('Location')

        logger.info('downloading binary from %s to %s.' % (binary_location, path))

        with open(os.path.join(path, 'factorio_alpha_%s_%s.tar.gz' % (arch, version)), 'wb') as handle:
            response = requests.get(binary_location, stream=True)

            for block in response.iter_content(1024):
                handle.write(block)

#https://www.factorio.com/get-download/0.13.3/alpha/linux64

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
