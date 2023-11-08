from django.urls import path
from . import views  # 1. подключаем файл views

urlpatterns = [
    path('', views.index),  # 2. добавляем ссылку на метод из файла views
]
