import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

from django.utils import timezone
import pytz

person = Person.objects.get(id=1)
print(person)
person.birthday = '2001-01-01'
person.save()

persons = Person.objects.filter(first_name='taro')
for i in persons:
  i.first_name = person.first_name.upper()
  i.save()



