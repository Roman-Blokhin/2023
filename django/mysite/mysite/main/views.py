from django.shortcuts import render

# ФУНКЦИЯ ПОДКЛЮЧЕНИЯ СТРАНИЦЫ, здесь подключаем шаблоны, чтобы не писать код в одном месте

def main(request):
    return render (request, 'main/index.html')

def about(request):
    return render (request, 'main/about.html')
