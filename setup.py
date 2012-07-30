# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup


version = __import__('model_report').__version__

LONG_DESCRIPTION = """
Django reports integrated with highcharts.
"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-model-report',
      version=version,
      author='Juan Pablo Martínez',
      author_email='jpma55@gmail.com',
      description='Django reports integrated with highcharts.',
      license='BSD',
      keywords='django, model, report, reports, highcharts, chart, charts',
      url='https://github.com/juanpex/django-model-report',
      packages=['model_report', ],
      package_data={'model_report': ['locale/*/LC_MESSAGES/*']},
      long_description=long_description(),
      install_requires=['django>=1.2.5', ],
      classifiers=['Framework :: Django',
                   'Development Status :: 3 - Alpha',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
