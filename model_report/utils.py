from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_unicode


def base_label(report, field):
    if hasattr(field, 'verbose_name'):
        return "%s" % field.verbose_name.title()
    return field

base_lookup_label = lambda report, field: "[%s] %s" % (field.model._meta.verbose_name.title(), field.verbose_name.title())

model_lookup_label = lambda report, field: "[%s] %s" % (report.model._meta.verbose_name.title(), field.verbose_name.title())


def sum_column(values):
    return Decimal(sum(values))
sum_column.caption = _('Total')


def avg_column(values):
    return Decimal(sum(values) / float(len(values))) if values else Decimal(0.00)
avg_column.caption = _('Average')


def count_column(values):
    return Decimal(len(values))
count_column.caption = _('Count')


def date_format(value):
    return value.strftime("%d/%m/%Y")


def usd_format(value):
    return 'USD %.2f' % Decimal(value)


def yesno_format(value):
    return _('Yes') if value else _('No')


class ReportValue(object):
    value = None

    def __init__(self, value):
        self.value = value

    def format(self, value):
        return value

    def text(self):
        return self.format(self.value)

    def __repr__(self):
        return force_unicode("%s" % self.text())

    def __unicode__(self):
        return force_unicode("%s" % self.text())

    def __str__(self):
        return "%s" % self.text()


class ReportRow(list):
    is_total = False
    is_caption = False

    def get_css_class(self):
        classes = []
        if self.is_total:
            classes.append('total')
        if self.is_caption:
            classes.append('caption')
        return " ".join(classes)

    def is_value(self):
        return self.is_total == False and self.is_caption == False
