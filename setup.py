from setuptools import setup
from Cython.Build import cythonize

setup(
    name="My shared object",
    ext_modules = cythonize("Shared_objects/*.pyx")
)