from django.urls import path
from . import views  # 1. подключаем файл views

urlpatterns = [
    path('', views.index, name='home'),  # 2. добавляем ссылку на метод из файла views
    path('about', views.about, name='about'),  # 3. прописываем имя для ссылки на страницу
]
