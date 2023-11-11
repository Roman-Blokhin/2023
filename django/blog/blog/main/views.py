from django.shortcuts import render
from django.http import HttpResponse  # 1. произвели импорт

# HttpResponse не может корректно выгрузить нам всю страницу, поэтому лучше использовать render
def index(request): # загружаем шаблон из папки templates
    return render(request, 'main/index.html')

def about(request):  # 2. создали метод
    return HttpResponse('<h3 style="color: ff0000"><i>Информация о компании</i></h3>') # 3. прописываем, что возвращаем