# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from app.models import Population, Browser, BrowserDownload

from model_report.report import reports, ReportAdmin
from model_report.utils import (avg_column, sum_column, count_column)


def men_format(value):
    return _(u'M %s' % value)


def women_format(value):
    return _(u'F %s' % value)


def men_label(report, field):
    return _("Mens")


class PopulationReport(ReportAdmin):
    model = Population
    fields = [
        'age',
        'men',
        'women',
        'self.total',
    ]
    list_filter = ('age',)
    list_order_by = ('age',)
    list_group_by = ('age',)
    type = 'report'
    group_totals = {
        'men': avg_column,
        'women': avg_column
    }
    report_totals = {
        'men': sum_column,
        'women': sum_column
    }
    override_field_formats = {
        'men': men_format,
        'women': women_format,
    }
    override_field_labels = {
        'men': men_label,
    }
    list_serie_fields = ('men', 'women',)


reports.register('population-report', PopulationReport)


def browser__name_label(report, field):
    return _("[Browser] Name")


def os__name_label(report, field):
    return _("[OS] Name")


class BrowserDownloadReport(ReportAdmin):
    model = BrowserDownload
    fields = [
        'download_date',
        'browser__name',
        'os__name',
        'username',
    ]
    list_filter = ('browser__name', 'os__name', 'download_date')
    list_order_by = ('download_date',)
    list_group_by = ('browser__name', 'os__name',)
    type = 'chart'
    override_field_labels = {
        'browser__name': browser__name_label,
        'os__name': os__name_label,
    }
    group_totals = {
        'download_date': count_column,
    }
    report_totals = {
        'download_date': count_column,
    }
    list_serie_fields = ('browser__name', 'os__name')
    chart_types = ('pie', 'column')


reports.register('browser-download-report', BrowserDownloadReport)


class BrowserReport(ReportAdmin):
    title = _('Browser with Inline Downloads')
    model = Browser
    fields = [
        'name',
    ]
    inlines = [BrowserDownloadReport]
    # list_filter = ('name',)
    list_order_by = ('name',)
    # list_group_by = ('browser__name', 'os__name',)
    type = 'report'
    # override_field_labels = {
    #     'browser__name': browser__name_label,
    #     'os__name': os__name_label,
    # }
    # group_totals = {
    #     'download_date': count_column,
    # }
    # report_totals = {
    #     'download_date': count_column,
    # }
    #list_serie_fields = ('browser__name', 'os__name')
    # chart_types = ('pie', 'column')


reports.register('browser-report', BrowserReport)
