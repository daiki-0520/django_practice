import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

persons = Person.objects.all()
for i in persons:
  print(i.id, i, i.salary)

person = Person.objects.get(first_name='taro')
print(person.id, person)

#filter(絞り込み　エラーにはならない　複数取得可能)
print('#############################################')
persons = Person.objects.filter(first_name='Jiro')
print(persons)

for i in persons:
  print(i.id, i)