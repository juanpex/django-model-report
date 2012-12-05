# -*- encoding: utf-8 -*-
from django.contrib import admin

from app.models import Population, Browser, BrowserDownload, OS, Support, Company, ResolutionByYear


admin.site.register(ResolutionByYear)
admin.site.register(Company)
admin.site.register(Population)
admin.site.register(Browser)
admin.site.register(OS)
admin.site.register(Support)
admin.site.register(BrowserDownload)
