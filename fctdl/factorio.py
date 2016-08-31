#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import requests, os, logging

from lxml import html

logger = logging.getLogger(__name__)

login_url = 'https://www.factorio.com/login'

versions_url = {
    'stable': 'https://www.factorio.com/download/stable',
    'experimental': 'https://www.factorio.com/download/experimental',
}

download_url = {
    'x86': 'https://www.factorio.com/get-download/%s/alpha/linux32',
    'x64': 'https://www.factorio.com/get-download/%s/alpha/linux64',
}

class Factorio:
    def __init__(self, username, password):
        self._session = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        logger.debug('requesting csrf token.')

        response = self._session.get(login_url, allow_redirects=False)

        login_page = html.fromstring(response.text)

        csrf_token = login_page.xpath("//input[@id='csrf_token']/@value")[0]

        assert len(csrf_token) > 0, 'csrf token was empty'

        payload = {
            'csrf_token': csrf_token,
            'username_or_email': username,
            'password': password,
            'action': 'Login',
        }

        logger.info('logging in.')
        logger.debug('using form data: %s' % payload)

        response = self._session.post('https://www.factorio.com/login', allow_redirects=False,
            data = payload,
        )

        if response.status_code != 302:
            raise Exception('failed to log in.')

    def download(self, version, arch, path):
        logger.info('requesting binary location.')
        response = self._session.get(download_url.get(arch) % version, allow_redirects=False)

        if response.status_code != 302:
            raise Exception('location request failed: %s' % response.text)
        elif 'Location' not in response.headers:
            raise Exception('No location received in headers: %s' % response.headers)

        binary_location = response.headers.get('Location')

        logger.info('downloading binary from %s to %s.' % (binary_location, path))

        with open(os.path.join(path, 'factorio_alpha_%s_%s.tar.gz' % (arch, version)), 'wb') as handle:
            response = requests.get(binary_location, stream=True)

            for block in response.iter_content(1024):
                handle.write(block)

    def list(self, branch):
        logger.info('requesting versions.')
        response = self._session.get(versions_url.get(branch), allow_redirects=False)

        if response.status_code != 200:
            raise Exception('version request failed.')

        version_page = html.fromstring(response.text)

        for version in version_page.xpath("//div[@class='container']/h3/text()"):
            print('* %s' % version.strip())

#https://www.factorio.com/get-download/0.13.3/alpha/linux64

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
