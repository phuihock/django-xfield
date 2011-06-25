from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='django-xfield',
    version='0.1.0',
    url='https://github.com/phuihock/django-xfield',
    license='GPLv3',
    author='Chang Phui Hock',
    author_email='phuihock@gmail.com',
    description="A Django utility package to handle zero or more form inputs of the same name.",
    long_description=long_description,
    include_package_data=True,
    packages=['xfield'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
    ],
)
