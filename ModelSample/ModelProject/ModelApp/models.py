from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True, null=True)
    salary= models.FloatField(null=True)
    memo = models.TextField(null=True)
    web_site = models.URLField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)

