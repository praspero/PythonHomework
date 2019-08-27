from setuptools import setup, find_packages

setup(
    name='pycalc',
    version='1.3',
    description='pure command-line calculator',
    author='Ihnatsi Baltsiukevich',
    packages=find_packages(),
    entry_points={'console_scripts': ['pycalc = calculator.pycalc:main']}
)
