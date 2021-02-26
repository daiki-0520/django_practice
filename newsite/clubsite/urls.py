from django.urls import path
from . import views

app_name = 'newsite'
urlpatterns = [
  path('home', views.home, name = 'home'),
  path('members', views.members, name = 'members'),
  path('id/<int:id>', views.id, name = 'id'),
]