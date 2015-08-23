from __future__ import print_function

from setuptools import find_packages, setup
import sys


install_requirements = []
if sys.version_info < (3, 4):
    install_requirements.append('enum34')


setup(
    name='inklevel',
    version='0.1',
    url='https://github.com/tom-mi/python-inklevel/',
    license='GPLv2',
    author='Thomas Reifenberger',
    tests_require=['pytest'],
    install_requires=install_requirements,
    author_email='tom-mi at rfnbrgr.de',
    description='Python wrapper for libinklevel',
    packages=find_packages(),
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Monitoring',
        ],
)
