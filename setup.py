import codecs
import os
import re

from setuptools import setup, find_packages


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as f:
        return f.read()


def find_version(*fp):
    file = read(*fp)
    match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        file,
        re.M,
    )
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


README = read('README.rst')

setup(
    name='pylogic',
    version=find_version('pylogic', '__init__.py'),
    description='Logic Programming for Python',
    long_description=README,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
    ],
    keywords='propositional logic kb inference knowledge',
    # url='http://github.com/lamcw/pylogic',
    author='lamcw',
    author_email='thomas@lamcw.com',
    license='MIT',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False)
