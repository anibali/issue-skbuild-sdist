from os import environ

if environ.get('SETUPTOOLS'):
    print('Using `setup` from setuptools.')
    from setuptools import setup
else:
    print('Using `setup` from skbuild.')
    from skbuild import setup

setup(
    name='skbuild-sdist',
    include_package_data=True,
)
