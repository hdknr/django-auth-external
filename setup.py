#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This file is part of "Django-auth-external"
#
#  mand is a Django based management interface for MySQL users and databases.
#
#  Copyright 2013 TACT Communications
#
#  Licensed under the Simplified BSD License;
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.freebsd.org/copyright/freebsd-license.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  NOTES
#
#  Create source distribution tarball:
#    python setup.py sdist --formats=gztar
#
#  Create binary distribution rpm:
#    python setup.py bdist --formats=rpm
#
#  Create binary distribution rpm with being able to change an option:
#    python setup.py bdist_rpm --release 7
#
#  Test installation:
#    python setup.py install --prefix=/usr --root=/tmp
#
#  Install:
#    python setup.py install
#  Or:
#    python setup.py install --prefix=/usr
#

######################################################
NAME='authx'
DESCRIPTION='Django-auth-external'
PACKAGES=['authx',]
GITHUB_USER="hdknr"
GITHUB_PROJECT="django-auth-external"
######################################################

import sys
import os
import glob
sys.path.insert(0, os.path.abspath('src'))

from setuptools import setup

# - Meta Info

from authx import get_version

SCRIPTS=glob.glob('scripts/*.py')
try:
    INSTALL_REQUIRES=[ r for r in open('requirements.txt').read().split('\n') if len(r)>0]
except:
    INSTALL_REQUIRES=[] 

# - readme

def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__=='__main__':
    setup(
        name = NAME,
        version = get_version(),
        license = 'Simplfied BSD License',
        author = 'Hideki Nara of LaFoaglia,Inc.',
        author_email = 'gmail [at] hdknr.com',
        maintainer = 'LaFoglia,Inc.',
        maintainer_email = 'gmail [at] hdknr.com',
        url = 'https://github.com/%s/%s' % (GITHUB_USER,GITHUB_PROJECT),
        description = DESCRIPTION,
        long_description = read('README.rst'),
        download_url = 'https://github.com/%s/%s' % (GITHUB_USER,GITHUB_PROJECT),
        platforms=['any'],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Library',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Simplifed BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ],
        package_dir = {'': 'src'},
        packages = PACKAGES,
        include_package_data = True,
        zip_safe = False,
        scripts=SCRIPTS,
    )
