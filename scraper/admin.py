from django.contrib import admin
from .models import Vacancies, WebSites, Selectors

# Register your models here.
admin.site.register(Vacancies)
admin.site.register(WebSites)
admin.site.register(Selectors)