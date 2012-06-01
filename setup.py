from setuptools import find_packages
from distutils.core import setup

setup(
    name='countria',
    version='0.8',
    url='http://github.com/geomin/django-countria',
    maintainer='Georg Kasmin',
    maintainer_email='georg@aquarianhouse.com',
    description='A full collection of countries, cities, state etc.',
    classifiers=['License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Global :: Countries'],
    license='BSD',
    platforms=['any'],
    install_requires=['lingua'],#pip
    packages=['countria'],
    package_dir={
        'countria': 'countria'
    },
    package_data={
        'countria': ['fixtures/*.json', 'locale/de/LC_MESSAGES/*.po']
    }
)
