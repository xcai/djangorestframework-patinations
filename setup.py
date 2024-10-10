import codecs
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

def read_me(filename):
    return codecs.open(filename, encoding='utf-8').read()


setup(
    name='drf-patinations',
    version='1.0.0',
    packages=['drf_pagination'],
    url='https://github.com/xcai/drf-patinations',
    download_url='https://github.com/xcai/drf-patinations',
    license='MIT',
    author='xcai',
    author_email='xxiaocai@163.com',
    description='Django REST framework additional patinations, e.g. DatatablePatination',
    long_description=read_me('README.md'),
    install_requires=[
        'djangorestframework',
    ],
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django REST Framework",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    keywords=["django", "rest", "drf", "pagination", "datatable", "django rest framework"],
    include_package_data=True,
    zip_safe=False,

)
