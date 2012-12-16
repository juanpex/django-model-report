# -*- coding: utf-8 -*-
import unittest
from django.test.client import Client

BASIC_GET_FOR_REPORT = {
    'resolution-by-year-report': '/resolution-by-year-report/?groupby=None&resolution=',
    'os-report': '/os-report/?company__name=',
    'population-report': '/population-report/?groupby=None&age=',
    'browser-download-report': '/browser-download-report/?groupby=None&browser__name=&os__name=&os__company__name=&download_date_0=&download_date_1=&chart_mode=&serie_field=&serie_op=',
    'browser-report': '/browser-report/?__all__=1',
    'browser-list-report': '/browser-list-report/?groupby=None&chart_mode=&serie_field=&serie_op=',
}


class ExampleCaseBasic(unittest.TestCase):
    fixtures = ['app', ]

    def test_basic_query(self):
        c = Client()
        response = c.post('/')
        self.assertEqual(response.status_code, 200)
        report_list = response.context['report_list']
        for report in report_list:
            response = c.get("/%s/" % report.slug)
            self.assertEqual(response.status_code, 200)
            report_rows = response.context['report_rows']
            if report_rows:
                raise ValueError('Not empty report_rows for "%s"' % report.slug)
            response = c.get(BASIC_GET_FOR_REPORT[report.slug])
            self.assertEqual(response.status_code, 200)
            report_rows = response.context['report_rows']
            if not report_rows:
                raise ValueError('Empty report_rows for "%s"' % report.slug)
