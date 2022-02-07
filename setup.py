from setuptools import Extension, setup
from Cython.Build import cythonize

#sourcefiles = ['calculator/calc.pyx', 'calculator/main.pyx']
#extensions = [Extension("calculator", sourcefiles)]

setup(
    name="Mysharedobject",
    package_dir={'calculator': ''},
    ext_modules = cythonize('calculator/calculator.pyx')
)