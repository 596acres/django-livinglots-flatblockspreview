from setuptools import setup, find_packages
import os

import livinglots_flatblockspreview


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='eric@596acres.org',
    name='django-livinglots-flatblockspreview',
    version=livinglots_flatblockspreview.__version__,
    description=("A Django app for previwing FlatBlock templates"),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/596acres/django-livinglots-flatblockspreview/',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.7.1',
        'django-braces==1.4.0',
        'django-classy-tags==0.5.1',
    ],
    packages=find_packages(),
    include_package_data=True,
)
