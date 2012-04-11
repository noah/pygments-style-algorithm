#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-algorithm',
    version='0.1',
    description='Algorithm theme (black and white) for algorithms.',
    long_description=open('README.rst').read(),
    keywords='pygments style algorithm',
    license='BSD',

    author='Noah K. Tilton',
    author_email='noahktilton@gmail.com',

    url='https://github.com/noah/pygments-style-algorithm',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    algorithm=pygments_style_algorithm:AlgorithmStyle''',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
