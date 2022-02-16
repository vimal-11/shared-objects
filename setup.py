from setuptools import Extension, setup
from Cython.Build import cythonize

sourcefiles = ['calculator/calculator.pyx', 'calculator/utility/utils.pyx']
extensions = [Extension("calculator", sourcefiles)]

setup(
    name="Mysharedobject",
    packages=["calculator", "calculator.utility"],
    package_dir = {'calculate': 'calculator', 'utility': 'utility'},
    #ext_modules = cythonize(['calculator/calculator.pyx', 'calculator/utility/utils.pyx'])
    ext_modules = cythonize(extensions)
)
