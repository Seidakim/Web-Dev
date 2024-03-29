from django.conf import settings
from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    city = models.CharField(max_length=255)
    address = models.TextField(default='')
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'salary':self.salary,
            'company':self.company.name,    
            
        }