# -*- encoding: utf-8 -*-
from django.contrib import admin

from app.models import Population, Browser, BrowserDownload, OS

admin.site.register(Population)
admin.site.register(Browser)
admin.site.register(OS)
admin.site.register(BrowserDownload)
