#!/usr/bin/env python

from distutils.core import setup

setup(
    name='jsonrpctcp',
    version='0.2',
    url='https://github.com/R242/jsonrpctcpt
    description='JSON-RPC (v2) over TCP sockets.',
    author='Josh Marshall',
    author_email='',
    packages=['jsonrpctcp',],
    install_requires=['six']
)

setup(name='jsonrpctcp',
      version='0.2.0',
      description='JSON-RPC (v2) over TCP sockets.',
      url='https://github.com/R242/jsonrpctcp',
      author='Alexander Larin',
      author_email='',
      license='MIT',
      packages=['jsonrpctcp'],
      install_requires=['six'],
      zip_safe=False)
