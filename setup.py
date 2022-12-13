# -*- coding: utf-8 -*-
"""partlets
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oraculum",
    version="0.0.1",
    author="Alexander Fedotov",
    author_email="alex.fedotov@aol.com",
    description="Oraculum - adaptive experimentation with the help of adaptive computations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oraculum-service/oraculum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
