#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name='space_rocket_state_controller',
	version='0.1.0',
	description='Space Rocket state controller',
	long_description='State controller fro space rocket',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'numpy'
	],
	entry_points='''
''')
