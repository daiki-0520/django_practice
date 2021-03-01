import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

#p = Person(
  #first_name = 'taro',
  #last_name='abe',
  #birthday = '2001-01-01', email = 'aa@example.com',
  #salary=1000, memo = 'memo', web_site='https://www.google.com'
#)
#p.save()

# classmethod create
Person.objects.create(
  first_name='Jiro', last_name='ito',
  email = 'ai@example.com',salary=20,
  memo='class', web_site=None
)
#取得又は作成
obj, created = Person.objects.get_or_create(
    first_name='daikikiki', last_name='ito',
    email = 'ai@example.com',salary=4000,
    memo='class', web_site=None
)

print(obj)
print(created)
