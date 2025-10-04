# setup.py
from setuptools import setup, find_packages

setup(
    name="netbox-scanner-plugin",
    version="1.0.0",
    description="Network discovery and scanner management for NetBox",
    url="https://github.com/your-username/netbox-scanner-plugin",
    author="sajad balaniyan",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-nmap",
        "netmiko",
    ],
    zip_safe=False,
)