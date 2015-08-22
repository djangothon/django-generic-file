from setuptools import setup, find_packages
from genericfile.meta import VERSION

setup(
    name='django-generic-file',
    version=str(VERSION),
    description="Django Generic File",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=['fileupload', 'django', 'file', 'upload'],
    author='Rajiv Subramanian M',
    author_email='rajiv.m1991@gmail.com',
    url='https://github.com/djangothon/django-generic-file',
    download_url='https://github.com/djangothon/django-generic-file/tarball/' + str(VERSION),
    install_requires=['Django', ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)
