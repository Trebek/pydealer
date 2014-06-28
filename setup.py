try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    README = f.read()

setup(
    name='pydealer',
    version='1.2.1',
    author='Alex Crawford',
    author_email='kebert406@yahoo.com',
    packages=['pydealer'],
    scripts=[],
    url='https://github.com/Trebek/pydealer',
    license='LICENSE.txt',
    description='A package for creating decks of playing cards.',
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3"
    ],
    keywords='playing cards deck game french standard 52',
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)