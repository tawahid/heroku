from django.db import models
from django.core.validators import RegexValidator


# Custom validators here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z .-]*$', 'No special characters are allowed.')
contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Contact number format: '+999999999'. Upto 15 digits.")


# Create your models here.
class StudioItems(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.CharField(max_length=560, null=True)

class MessagesModel(models.Model):
    name = models.CharField(validators=[alphanumeric],max_length=100, blank=False)
    email = models.EmailField(blank=False)
    contact = models.CharField(validators=[contact_regex], max_length=17, blank=True, null=True)
    message = models.CharField(validators=[alphanumeric],max_length=1000, blank=False)