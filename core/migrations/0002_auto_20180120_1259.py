# Generated by Django 2.0 on 2018-01-20 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z .-]*$', 'No special characters are allowed.')])),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Contact number format: '+999999999'. Upto 15 digits.", regex='^\\+?1?\\d{9,15}$')])),
                ('message', models.CharField(max_length=1000, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z .-]*$', 'No special characters are allowed.')])),
            ],
        ),
        migrations.AlterField(
            model_name='studioitems',
            name='description',
            field=models.CharField(max_length=560, null=True),
        ),
    ]
