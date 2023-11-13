from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('about/', include('main.urls')),
]