from codecs import open as codecs_open
from setuptools import setup, find_packages


setup(
    name='pyrandimg',
    version='0.0.1',
    description=u"Python package for generating beautiful random images using Rand-Img provider for Fake package",
    long_description='Provider for joke2k/faker package. It generates random image and gif URLs and download them',
    classifiers=[],
    keywords='',
    author=u"Siro Díaz",
    author_email='siro_diaz@yahoo.com',
    url='https://github.com/SiroDiaz/pyrandimg',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Faker'
    ],
)
