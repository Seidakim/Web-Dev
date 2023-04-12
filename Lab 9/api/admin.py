from django.contrib import admin

from .models import Company,Vacancy


admin.site.register((Company,Vacancy))
# Register your models here.
