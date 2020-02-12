import json
from django.db import models


class WebSites(models.Model):
    jobs_web_site = models.URLField(max_length=300)

    def __str__(self):
        return self.jobs_web_site


class VacanciesManager(models.Manager):
    def get_vacancies(self):
        vacancies = super().get_queryset()
        for vacancy in vacancies:
            vacancy.description = json.loads(vacancy.description)
        return vacancies


class Vacancies(models.Model):
    title = models.CharField(max_length=300, null=True)
    url = models.URLField(max_length=200, null=True)
    description = models.CharField(max_length=25000, null=True)
    company_web_site = models.URLField(max_length=200, null=True)
    job_info = models.CharField(max_length=500, null=True)
    jobs_web_site = models.ForeignKey(WebSites, on_delete=models.CASCADE, default='')

    objects = VacanciesManager()

    def __str__(self):
        return self.title


class Selectors(models.Model):
    jobs_web_site = models.ForeignKey(WebSites, on_delete=models.CASCADE, default='')
    vacancy_link = models.CharField(max_length=150)
    next_page = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    company_web_site = models.CharField(max_length=150)
    job_info = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)

    def __str__(self):
        return f'Selectors for {self.jobs_web_site}'
