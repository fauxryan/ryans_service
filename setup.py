# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from ryans_service import __version__


setup(
    name="ryans_service",
    version=__version__,
    description="CherryPy based microservice.",
    maintainer="",
    packages=["ryans_service"],
    platforms=["any"]
)
