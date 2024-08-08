from setuptools import setup, find_packages

setup(
    name='darts-timeseries-forecaster',
    version='1.0.7',
    author='Peter Peerdeman',
    packages=find_packages(),
    install_requires=[
        'darts==0.29.0'
    ],
)
