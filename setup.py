# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in library_management/__init__.py
from library_management import __version__ as version

setup(
	name='library_management',
	version=version,
	description='library app for managing books and articles',
	author='lee22jar',
	author_email='info@library.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
