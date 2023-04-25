from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in easyprospection/__init__.py
from easyprospection import __version__ as version

setup(
	name="easyprospection",
	version=version,
	description="The Easy prospection is a prototype of a frappe app to make the prospection process easy for sales teams",
	author="DARCOS",
	author_email="contact@darcos.dz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
