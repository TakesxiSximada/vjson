#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import (
    setup,
    find_packages,
    )

src = 'src'
here = lambda path: os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
get_requires = lambda path: open(here(path), 'rt').readlines()

readme_path = here('README.rst')

requirements_txt = 'requirements/install.txt'
if not (sys.version_info.major >= 3 and sys.version_info.minor >= 2):
    requirements_txt = 'requirements/install-py2.txt'
install_requirements = get_requires(requirements_txt)
test_requirements = get_requires('requirements/test.txt')

setup(
    name='vjson',
    version='0.1',
    url='https://github.com/TakesxiSximada/vjson',
    download_url='https://github.com/TakesxiSximada/vjson/master.zip',
    license='MIT',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="vjson creates an object to serialize the only of the type specified in JSONSchema. It works like a json module.",
    long_description=open(readme_path, 'rt').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=find_packages(src),
    package_dir={'': src},
    namespace_packages=[
        ],
    package_data={},
    include_package_data=True,
    install_requires=install_requirements + test_requirements,
    tests_requires=test_requirements,
    entry_points='''
    [console_scripts]
    '''
    )
