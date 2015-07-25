from codecs import open
from os import path

from setuptools import setup

from rtfdoc import __version__

base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'LICENSE'), encoding='utf-8') as f:
    LICENSE = f.read()

setup(
    name='rtfdoc',
    version=__version__,
    description='create beautiful and intelligent markdown documentation',
    long_description='''rtfdoc is a tool that makes it easy to create intelligent and beautiful documentation for software projects, consisting of multiple markdown sources.''',
    url='http://rtfdoc.com',
    author='Guillaume Vincent',
    author_email='guillaume@oslab.fr',
    license=LICENSE,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities',
    ],
    keywords='markdown documentation',
    packages=['rtfdoc'],
    install_requires=[
        'commonmark',
    ],
    entry_points={
        'console_scripts': [
            'rtfdoc-build = rtfdoc:main',
            'rtfdoc-quickstart = rtfdoc.quickstart:main',
        ],
    },
)
