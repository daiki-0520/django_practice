import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Places, Restaurants

places = [
  ('motomachi', 'yokohama'), ('tukizi', 'Tokyo')
]
restaurants =[
  'A', 'B'
]

for place_name, place_address in places:
  p = Places(name=place_name, address = place_address)
  print(p)
  p.save()
  for restaurant_name in restaurants:
    r = Restaurants(place = p, name = restaurant_name)
    r.save()
