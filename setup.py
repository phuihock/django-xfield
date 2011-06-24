from setuptools import find_packages, setup


setup(
    name='django-xfield',
    version='0.1',
    url='https://github.com/phuihock/django-xfield',
    license='GPLv3',
    author='Chang Phui Hock',
    author_email='phuihock@gmail.com',
    description="A Django utility package to handle zero or more inputs of the same name.",
    include_package_data=True,
    zip_safe=False,
    packages=['xfield'],
    package_dir={'': '.'},
    install_requires=(
    ),
)
