#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.gazetteer.export',
    namespace_packages=['mapzen', 'mapzen.gazetteer'],
    version='0.21',
    description='Simple Python wrapper for managing Mapzen Gazetteer export-related functions',
    author='Mapzen',
    url='https://github.com/thisisaaronland/py-mapzen-gazetter-export',
    install_requires=[
        'requests',
        'geojson',
        'woe.isthat'
        ],
    dependency_links=[
          'https://github.com/thisisaaronland/py-woe-isthat/tarball/master#egg=woe-isthat-0.14',
        ],
    packages=packages,
    scripts=[
        'scripts/mzg-concordify',
        ],
    download_url='https://github.com/thisisaaronland/py-mapzen-gazetteer-export/releases/tag/v0.1',
    license='BSD')
