#! /usr/bin/env python3

from setuptools import find_packages, setup

__version__ = '0.0.1'

requires = [
    'pycryptodome'
]

DESCRIPTION = """Used by AES encrypt or decrypt.
AES/ECB/PKCS5Padding  same as aes in java default.
"""

setup(
    name='aes-sha1prng',
    version=__version__,
    description='AES/ECB/PKCS5Padding Python library',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author='BobDu',
    author_email='i@bobdu.cc',
    url='https://github.com/Bob-Du/aes-sha1prng',
    packages=find_packages(),
    install_requires=requires,
    zip_safe=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ),
)
