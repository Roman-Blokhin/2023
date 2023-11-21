from django.shortcuts import render
from django.http import HttpResponse  # 1. произвели импорт

# HttpResponse не может корректно выгрузить нам всю страницу, поэтому лучше использовать render
def index(request): # загружаем шаблон из папки templates
    data = {  # 4. создали словарь для вызова из него данных
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)  # 3. третьим параметром выводим переменную - словарь

def about(request):  # 2. создали метод
    data = {
        'values': ['some', '123', 'welcome']  # 5. создали список данных
    }
    return render(request, 'main/about.html', data)
    # return HttpResponse('<h3 style="color: ff0000"><i>Информация о компании</i></h3>') # 3.прописываем, что возвращаем