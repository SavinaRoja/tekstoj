"""
"""

from distutils.core import setup
#from setuptools import setup


def long_description():
    with open('README.md', 'r') as readme:
        readme_text = readme.read()
    return(readme_text)

setup(name='tekstoj',
      version='0.0.1',
      description='Interface to text conversations via Twilio',
      long_description=long_description(),
      author='Paul Barton',
      author_email='pablo.barton@gmail.com',
      url='https://github.com/SavinaRoja/tekstoj',
      package_dir={'': 'src'},
      packages=['tekstoj'],
#      package_data={},
#      scripts=['scripts/'],
      data_files=[('', ['README.md'])],
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Programming Language :: Python :: 3',
                   'Operating System :: OS Independent'],
      install_requires=['docopt', 'twilio==6.0rc10', 'flask', 'sqlalchemy']
      )

