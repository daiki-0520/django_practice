from django.shortcuts import render


class Member:
    def __init__(self, id, name, join_at, picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
  Member(0,'taro','2018/04/01', 'img/taro.jpg'),
  Member(1, 'jiro', '2019/04/01', 'img/jiro.jpg'),
  Member(2, 'hanako', '2019/05/02', 'img/hanako.jpg'),
  Member(3, 'yoshiko', '2018/10/01', 'img/yoshiko.jpg')
]
# Create your views here.
def home(request):
    return render(request, 'home.html')


def members(request):
    return render(request, 'members.html', context = {
      'members': member_list
    })


def id(request, id):
    return render(request, 'id.html', context = {
      'member': member_list[id]
    })