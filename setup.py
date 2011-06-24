from setuptools import find_packages, setup


setup(
    name='django-xfield',
    version='0.1',
    url='https://github.com/phuihock/django-xfield',
    license='GPLv3',
    author='Chang Phui Hock',
    author_email='phuihock@gmail.com',
    description="Handle input field that can be added/deleted any number of times by client, possibly using Javascript.",
    include_package_data=True,
    zip_safe=False,
    packages=['xfield'],
    package_dir={'': '.'},
    install_requires=(
    ),
)
