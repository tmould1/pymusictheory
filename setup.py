from setuptools import setup, find_packages

setup(
    name='pychord',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='none',
    description='none',
    long_description=open('README.md').read(),
    install_requires=[],
    url='REPOSITORY_URL',
    author='TM',
    author_email='AUTHOR_EMAIL'
)