#!/usr/bin/env python

# from distutils.core import setup, find_packages
from setuptools import setup, find_packages

setup(name='justvpn'
      , version='0.4.0'
      , description='An library which used for connect to JUST VPN'
      , long_description=open('README.md').read()
      , long_description_content_type="text/markdown"
      , author='Kos Wu'
      , author_email='ws00298046@163.com'
      , license='MIT License'
      , packages=["justvpn"]
      , platforms=["all"]
      , url='https://github.com/Koswu/JustVpn'
      , python_requires=">=2.6, !=3.0.*, !=3.2.*, !=3.3.*"
      , install_requires=["beautifulsoup4", "requests", "lxml"]
      )
