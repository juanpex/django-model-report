 


Django Model Report
===================

django-model-report is a Django application and library for reports integrated with highcharts.


[![Build Status](https://travis-ci.org/juanpex/django-model-report.png)](https://travis-ci.org/juanpex/django-model-report)

now maintained by  [@jelenak](https://github.com/jelenak "@jelenak")
--------------------------------------------------------------------

Demo
====

http://django-model-report.herokuapp.com


Documentation
=============

https://django-model-report.readthedocs.org/en/latest/

ForeignKey queryset in main report.py file:

    list_filter_queryset = {
        'user': {'groups__in': [13, 34]},
    }

Custom widget:

    list_filter_widget = {
        'state':  SelectMultiple(),
    }

Contribute
==========

Clone the repo and help to be better this app :)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/juanpex/django-model-report/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

