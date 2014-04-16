# -*- coding: utf-8 -*-
import cStringIO as StringIO
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(report, template_src, context_dict, pdf_encoding='UTF-8'):
    """
        Render the report results to pdf format.

        Keyword arguments:
        report -- a report instance
        template_src -- template file path
        context_dict -- context dictionary
        pdf_encoding -- encoding to render string
    """
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    from xhtml2pdf import pisa
    pdf = pisa.CreatePDF(StringIO.StringIO(html.encode(pdf_encoding)), result, encoding=pdf_encoding)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s.pdf' % report.slug
    else:
        response = HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

    result.close()
    return response

