from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', context = {'value': 'HEllo'})

def home(request,first_name, last_name):
    my_name = f'{first_name} {last_name}'
    favorite_fruits = ['app', 'banana']
    my_info = {
        'name': 'daiki',
        'age': 18,
		}
    status = 20
    return render (request, 'home.html', context = {
    		'my_name': my_name,
        'my_info': my_info,
        'favorite_fruits': favorite_fruits,
			  'status': status
    })


def sample1(request):
	  return render(request, 'sample1.html')

def sample2(request):
	  return render(request, 'sample2.html')

def sample(request):
		name = 'daiki'
		height = 170
		weight = 72
		bmi = weight / (height / 100)**2
		page_url = 'https://www.google.com'
		favorite_fruits = [
			'apple', 'banana', 'aiueo'
		]
		msg = """hello
		my name is
		daiki
		"""
		msg2 = '1234567890'
		return render(request, 'sample.html', context = {
			'name': name,
			'bmi': bmi,
			'page_url': page_url,
			'fruits': favorite_fruits,
			'msg': msg,
			'msg2': msg2
		})