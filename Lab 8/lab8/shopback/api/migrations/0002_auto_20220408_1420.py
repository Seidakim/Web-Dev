# Generated by Django 3.2.12 on 2022-04-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('cat_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product_lol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('cat_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(default=0),
        ),
    ]