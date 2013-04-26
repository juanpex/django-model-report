# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('model_report').__version__


LONG_DESCRIPTION = """
django-model-report
===================

django reports integrated with highcharts

    $ git clone git://github.com/juanpex/django-model-report.git
"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-model-report',
      version=version,
      author='juanpex',
      author_email='jpma55@gmail.com',
      description='Django reports integrated with highcharts.',
      license='BSD',
      keywords='django, model, report, reports, highcharts, chart, charts',
      url='https://github.com/juanpex/django-model-report',
      packages=find_packages(),
      include_package_data=True,
      long_description=long_description(),
      install_requires=['django>=1.3',
                        'BeautifulSoup', #'bs4',
                       ],
      extras_require = {
          'pdf':  ["pisa",
                   'reportlab',
                   'html5lib'],
          'xls': ['xlwt==0.7.4'],
      },       
      classifiers=['Framework :: Django',
                   'Development Status :: 3 - Alpha',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
