# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from model_report.report import reports


def report_list(request):
    context = {
        'report_list': reports.get_reports()
    }
    return render_to_response('model_report/report_list.html', context, context_instance=RequestContext(request))


def report(request, slug):
    report_class = reports.get_report(slug)
    if not report_class:
        raise Http404
    context = {
        'report_list': reports.get_reports()
    }
    report = report_class(request=request)
    return report.render(request, extra_context=context)
