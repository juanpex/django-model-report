# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


AGE_IN_YEARS = enumerate(['Less than one year', '1 year'] + ['%s years' % x for x in range(2, 100)] + ['100 or more years', ])

RESOLUTION_CHOICES = (
    ('Higher', 'Higher'),
    ('1024x768', '1024x768'),
    ('800x600', '800x600'),
    ('640x480', '640x480'),
    ('Other', 'Other'),
)


class ResolutionByYear(models.Model):
    date = models.DateTimeField(_('Date'))
    resolution = models.CharField(_('Resolution'), max_length=10, choices=RESOLUTION_CHOICES, blank=False, null=False)
    percentage = models.PositiveIntegerField(_('Percentage'), default=0)

    class Meta:
        verbose_name = _('Resolution by year')
        verbose_name_plural = _('Resolutions by year')

    def date_text(self):
        return u'%s - %s' % (self.date.strftime('%B %Y'), self.get_resolution_display())

    def __unicode__(self):
        return u'%s - %s: %s' % (self.date.strftime('%B %Y'), self.get_resolution_display(), self.percentage)


class Population(models.Model):
    age = models.IntegerField(_('Age'), choices=AGE_IN_YEARS)
    men = models.IntegerField(_('Men'))
    women = models.IntegerField(_('Women'))

    def total(self):
        return self.men + self.women

    class Meta:
        verbose_name = _('Population')
        verbose_name_plural = _('Populations')

    def __unicode__(self):
        return u'With %s: %s' % (self.get_age_display().lower(), self.total())


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=25)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _("Companies")

    def __unicode__(self):
        return self.name


class OS(models.Model):
    name = models.CharField(_('Name'), max_length=25)
    company = models.ForeignKey(Company, verbose_name=_('Company'), null=True, blank=True)

    class Meta:
        verbose_name = _('OS')
        verbose_name_plural = _("OS's")

    def __unicode__(self):
        return self.name


class Support(models.Model):
    name = models.CharField(_('Name'), max_length=25)

    class Meta:
        verbose_name = _('Support')
        verbose_name_plural = _("Supports")

    def __unicode__(self):
        return self.name


class Browser(models.Model):
    name = models.CharField(_('Name'), max_length=25)
    is_active = models.BooleanField(_('Is Active?'), default=True)
    run_on = models.ManyToManyField(OS, verbose_name=_('Run On'), related_name='browsers', blank=True, null=True)
    supports = models.ManyToManyField(Support, verbose_name=_('Supports'), related_name='browsers', blank=True, null=True)

    class Meta:
        verbose_name = _('Browser')
        verbose_name_plural = _('Browsers')

    def __unicode__(self):
        return self.name


class BrowserDownload(models.Model):
    download_date = models.DateField(_('Download date'), default=datetime.date.today)
    browser = models.ForeignKey(Browser)
    os = models.ForeignKey(OS, null=True, blank=True)
    username = models.CharField(_('Username'), max_length=25)
    download_price = models.DecimalField(_('Download price'), decimal_places=2, max_digits=10, default=0)

    class Meta:
        verbose_name = _('Browser Download')
        verbose_name_plural = _('Browser Downloads')

    def __unicode__(self):
        return self.username
