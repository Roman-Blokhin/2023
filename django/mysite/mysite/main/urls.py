from django.urls import path, include
from . import views

# ПОДКЛЮЧАЕМ ССЫЛКИ НА СТРАНИЦЫ
urlpatterns = [
    path('', views.main),
    path('about/', views.about),
]