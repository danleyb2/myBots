#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='YourAppName',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='OpenShift App',
    # GETTING-STARTED: set author name (your name):
    author='Nyaundi Brian',
    # GETTING-STARTED: set author email (your email):
    author_email='example@example.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'requests==2.8.1',
        'python-instagram',
		'authomatic',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/',
		'https://pypi.python.org/simple/requests/',
		'https://pypi.python.org/simple/authomatic/',
        'https://pypi.python.org/simple/python-instagram/'
    ],
)
