from setuptools import Extension, setup
from Cython.Build import cythonize

#extensions = [Extension("*", ["*.pyx"])]

setup(
    name="Mysharedobject",
    ext_modules = cythonize("calculator/*.pyx")
)