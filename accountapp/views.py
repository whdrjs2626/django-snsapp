from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'accountapp/hello_world.html') # 첫번쨰 인자는 request, 두번째는 템플릿 명
