from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from .models import Women


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

# class Myclass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7],
    при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес,
    Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер,
    фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус»
    (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},

]


def index(request):
    posts = Women.published.all()
    data = {'title': 'Главная страница',
            'menu': menu,
            # 'float': 28.56,
            # 'lst': [1, 2, 'abc', True],
            # 'set': {1, 2, 3, 4, 5},
            # 'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            # 'obj': Myclass(10, 20),
            # 'url': slugify('The main page')
            'posts': posts,
            }

    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1}
    return render(request, 'post.html', data)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exeption):
    return HttpResponse('<h1>Страница не найдена</h1>')
