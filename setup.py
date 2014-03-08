import os
from setuptools import setup


setup(
		name='django-openlavaweb',
		version='1.0',
		packages=['scheduler'],
		include_package_data=True,	
		license="GPL 3",
		description="Scheduler tools provides a standard API For popular job schedulers."
		author="David Irvine",
		author_email="irvined@gmail.com",
		classifiers=[
			'Environment :: Web Environment',
			'Programming Language :: Python',
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 2.7',
			'Intended Audience :: Science/Research',
			'Intended Audience :: System Administrators',
			'Topic :: Scientific/Engineering',
			],
		)
