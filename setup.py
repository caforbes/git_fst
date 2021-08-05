from setuptools import setup, find_packages
import os

NAME = 'git_fst'
VERSION = "1.0"

PROJECT_ROOT = os.path.dirname(__file__)
with open(os.path.join(PROJECT_ROOT, "README.md"), "r", encoding="utf-8") as rm:
    long_description = rm.read()

setup(name=NAME,
      version=VERSION,
      description='An FST morphological analyzer for the Gitksan language',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/caforbes/git_fst',
      author='Clarissa Forbes',
      author_email='for.c.forbes@gmail.com',
      license='CC BY-NC-ND 4.0',
      packages=find_packages() + ['config'],
      include_package_data=True)
