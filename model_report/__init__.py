from model_report.report import ReportAdmin


class ReportInstanceManager(object):

    _register = {}

    def __init__(self):
        self._register = {}

    def register(self, slug, rclass):
        if slug in self._register:
            raise ValueError('Slug already exists: %s' % slug)
        report = rclass()
        setattr(report, 'slug', slug)
        self._register[slug] = report

    def get_report(self, slug):
        return self._register.get(slug, None)

    def get_reports(self):
        return self._register.values()


reports = ReportInstanceManager()
