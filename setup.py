#!/usr/bin/env python2

from distutils.core import setup

setup(name="Repo Manager",
      version="0.1",
      description="Generates manifests for Google's Repo tool",
      author="Ryan Aghdam",
      author_email="ryan@aghdam.org",
      packages=['RepoManager'],
      package_dir={'RepoManager': 'src/RepoManager'},
      scripts=['src/repo-manager'])
      
