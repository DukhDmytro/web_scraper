from django.db import models


class WebSites(models.Model):
    jobs_web_site = models.CharField(max_length=300, default='')


class Vacancies(models.Model):
    title = models.CharField(max_length=300, default='')
    url = models.CharField(max_length=200, default='')
    summary = models.CharField(max_length=600, default='')
    description = models.CharField(max_length=6000, default='')
    company_web_site = models.CharField(max_length=200, default='')
    experience = models.CharField(max_length=200, default='')
    info = models.CharField(max_length=300, default='')
    jobs_web_site = models.ForeignKey(WebSites, on_delete=models.CASCADE, default='')

