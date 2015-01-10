try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    README = f.read()

setup(
    name='pydealer',
    version='1.4.0',
    author='Alex Crawford',
    author_email='kebert406@yahoo.com',
    packages=['pydealer'],
    scripts=[],
    url='https://github.com/Trebek/pydealer',
    download_url='https://pypi.python.org/pypi/pydealer',
    license='GPLv3',
    description='A package for constructing decks of playing cards, for games.',
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Games/Entertainment",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3"
    ],
    keywords='playing cards deck games french standard 52 poker blackjack',
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)