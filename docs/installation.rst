Installation
============

django-model-report is on the Python Package Index (PyPI),
so it can be installed with standard Python tools like pip or easy_install.::

    $ pip install django-model-report


* Add the ``model_report`` directory to your Python path.

* Add ``model_report`` to your ``INSTALLED_APPS`` setting.

* Create file "reports.py" within any application directory (just like admin.py).

* Edit the file "reports.py" and register your reports like this::

        from anyapp.models import AnyModel
        from model_report.report import reports, ReportAdmin

        class AnyModelReport(ReportAdmin):
            title = _('AnyModel Report Name')
            model = AnyModel
            fields = [
                'anymodelfield',
            ]
            list_order_by = ('anymodelfield',)
            type = 'report'

        reports.register('anymodel-report', AnyModelReport)

* Activate your reports calling the autodiscover in ``urls.py`` (just like admin.py).::

        from model_report import report
        report.autodiscover()

* Add reports urls.::

    urlpatterns = patterns('',
        ...
        (r'', include('model_report.urls')),
        ...
    )