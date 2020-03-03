from setuptools import setup
setup(
  name = 'SQLtime',
  packages = ['SQLtime'],
  version = '1.0',
  license='MIT',
  description = 'Python lib to automate time based SQLi',   # Give a short description about your library
  author = 'Nishit',
  author_email = 'nishit@mailfence.com',
  url = 'https://github.com/nishitm/SQLtime',
  download_url = '',
  keywords = ['Blind time based SQL injection', 'Pentesting', "AppSec"],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Intended Audience :: Pentesters',
    'Topic :: Software Development :: Build Tools',
    'License :: MIT',
    'Programming Language :: Python :: 3.7'
  ],
)
