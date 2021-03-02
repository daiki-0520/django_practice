import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

print(Students.objects.all())

print(Students.objects.count())
print(Students.objects.filter(name='退路'.count())
#件数、最大値、最小値、平均値、平均値、合計
from django.db.models import Count, Max, Min, Avg, Sum
print(Studnets.objects.aggregate(Count('pk'), Max('pk'), Min('pk')))


#GROUP BY:
print(Students.objects.values('name').annotate(
  Max('pk'), Min('pk')
))


for student in Students.objects.all():
  print(student.name, student.school.name, student.school)

for student in Students.objects.filter(school__name = '南高校').all():
  print(student.name, student.school.name, student.school)
  