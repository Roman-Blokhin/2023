from django.shortcuts import render
from django.http import HttpResponse  # 1. произвели импорт

def index(request):  # 2. создали первый метод
    return HttpResponse('<h1>Проверка работы</h1>')  # 3. прописываем, что возвращаем

def about(request):
    return HttpResponse('<h3 style="color: ff0000"><i>Информация о компании</i></h3>')