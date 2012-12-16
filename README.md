Django Model Report
===================

django reports integrated with highcharts


[![Build Status](https://travis-ci.org/juanpex/django-model-report.png)](https://travis-ci.org/juanpex/django-model-report)

Demo
====

http://django-model-report.herokuapp.com


Installation
============

* Add the ``model_report`` directory to your Python path.

* Add ``model_report`` to your ``INSTALLED_APPS`` setting.

* Create file "reports.py" within any application directory (just like admin.py).

* Edit the file "reports.py" and register your reports like this:

        from app.models import Browser
        from model_report.report import reports, ReportAdmin

        class BrowserReport(ReportAdmin):
            title = _('Browser with Inline Downloads')
            model = Browser
            fields = [
                'name',
            ]
            list_order_by = ('name',)
            type = 'report'

        reports.register('browser-report', BrowserReport)

* Activate your reports calling the autodiscover in ``urls.py`` (just like admin.py).

        from model_report import report
        report.autodiscover()

* Add reports urls

    urlpatterns = patterns('',
        ...
        (r'', include('model_report.urls')),
        ...
    )


Configuration
=============

Extend your reports ``from model_report.report import ReportAdmin``

    class ReportExample(ReportAdmin):
        pass

* Atributes

    ``title``:

    Title of the report.

    ``template_name``:

    Template file name to render the report.

    ``exports``:

    List of allowed export formats.

    Example:

        exports = ('excel', 'pdf')

    ``model``:

    Django model

    ``fields``:

    List of model fields to be listed.

    ``list_filter``:

    List of fields to filter data.

    ``list_order_by``:

    List of fields to order data.

    ``list_group_by``:

    List of fields to group data.

    ``type``:

    "report" for only report.

    "chart" for report and show chart graphic results.

    ``group_totals``:

    Dictionary with field name as key and function to calculate their values.
    This row is displayed after each group as their totals.

    Example:

        group_totals = {
            'men': sum_column,
            'women': sum_column
        }

    ``report_totals``:

    Dictionary with field name as key and function to calculate their values.
    This row is displayed at the end of the report as the totals of all results.

    Example:

        report_totals = {
            'men': avg_column,
            'women': avg_column
        }

    ``override_field_values``:

    Dictionary with field name as key and function to parse their original values.


    Example:

        override_field_values = {
            'men': men_format,
            'women': women_format
        }

    ``override_field_formats``:

    Dictionary with field name as key and function to parse their value after ``override_field_values``.


    Example:

        override_field_formats = {
            'men': men_format,
            'women': women_format
        }

    ``override_field_labels``:

    Dictionary with field name as key and function to parse the column label.


    Example:

        override_field_labels = {
            'men': men_label
        }

    ``list_serie_fields``:

    List of fields to group by results in chart.

    ``chart_types``:

    List of highchart types.

    Example:

        chart_types = ('pie', 'column')

    ``inlines``:

    List of other's Report related to the main report.


Contribute
==========

Clone the repo and help to be better this app :)
