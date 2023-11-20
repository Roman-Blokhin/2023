"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# ОБОЗНАЧЕНЫ ССЫЛКИ И КУДА ОНИ ВЕДУТ - ОТСЛЕЖИВАНИЕ URL АДРЕСОВ

urlpatterns = [
    path('admin/', admin.site.urls),  # ПРИ ИСПОЛЬЗОВАНИЯ ССЫЛКИ ОТКРЫВАЕТСЯ ПАНЕЛЬ АДМИНИСТРАТОРА
    path('main/', include('main.urls')),  # отслеживаем главную страницу, url для нее не передаем
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # добавляем, чтобы статические файлы подключились
