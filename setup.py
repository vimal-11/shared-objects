from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [Extension("*", ["*.pyx"])]

setup(
    name="My shared object",
    ext_modules = cythonize(extensions)
)