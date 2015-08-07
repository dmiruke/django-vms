import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-vms',
	version='0.1',
	packages=['vms'],
	include_package_data=True,
	license='Apache License',  # example license
	description='A simple Django app to manage Video on Web-Page.',
	long_description=README,
	url='http://github.com/sungtaek/django-vms',
	author='Sungtaek',
	author_email='leesungtae@gmail.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache License', # example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		# Replace these appropriately if you are stuck on Python 2.
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
