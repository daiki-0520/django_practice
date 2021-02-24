from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html', context = {'value': 'HEllo'})

def home(request):
    my_name = 'daiki'
    favorite_fruits = ['app', 'banana']
    my_info = {
      'name': 'daiki',
      'age' : 18
    }
    return render (request, 'home.html', context = {
      'my_name': my_name,
      'my_info': my_info,
      'favorite_fruits': favorite_fruits
    })


def sample1(request):
	return render(request, 'sample1.html')

def sample2(request):
	return render(request, 'sample2.html')