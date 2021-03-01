import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Schools, Prefectures

prefectures = ['東京', '大阪']
schools = ['東高校', '西高校', '北高校', '南高校']
students = ['daiki', 'rin', 'aiu']

def insert_records():
  for prefecture_name in prefectures:
    prefecture = Prefectures(
      name=prefecture_name
    )
    prefecture.save()

  for i in schools:
    school = Schools(
      name = i,
      prefecture=prefecture
    )
    school.save()

  for i in students:
    student = Students(
      name=i, age=17,
      major='物理', school = school
    )
    student.save()


def select_student():
  students = Students.objects.all()
  for i in students:
    print(i.id, i.name, i.school.id, i.school.name, i.school.prefecture.id, i.school.prefecture.name)
select_student()