from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    category_id = models.IntegerField(default=0)
    def to_json(self):
        info = {
            'id':self.id,
            'name' :self.name,
            'price' :self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
            'category_id':self.category_id,
        }
        return info

class Category(models.Model):
    name = models.CharField(max_length=255)
    def to_json(self):
        info = {
            'id':self.id,
            'name':self.name,
        }
        return info


class Product_lol(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    cat_id = models.IntegerField(default=0)
    def to_json(self):
        info = {
            'id':self.id,
            'name' :self.name,
            'price' :self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
            'category_id':self.category_id,
        }
        return info

class Producct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    cat_id = models.IntegerField(default=0)
    def to_json(self):
        info = {
            'id':self.id,
            'name' :self.name,
            'price' :self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
            'cat_id':self.cat_id,
        }
        return info