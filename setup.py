from setuptools import find_packages
from setuptools import setup

import os


install_requires = [
    'chainer >=3.5.0, <5.0',
    'mpi4py',
]


if os.environ.get('READTHEDOCS', None) == 'True':
    install_requires.remove('mpi4py')  # mpi4py cannot be installed without MPI

setup(
    name='chainermn',
    version='1.3.1',
    description='ChainerMN: Multi-node distributed training with Chainer',
    author='Takuya Akiba',
    author_email='akiba@preferred.jp',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=['mock',
                   'pytest'],
)
