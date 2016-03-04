# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='dharma_center_erp',
    version=version,
    description='ERP plattform for Dharma Center',
    author='FPMT ',
    author_email='geral@pedropalacios.net',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
