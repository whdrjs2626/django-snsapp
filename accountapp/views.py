from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input') # POST 요청의 폼에서 hello_world_input인 데이터를 가져와라

        new_hello_world = HelloWorld() # HelloWorld 객체(모델) 생성
        new_hello_world.text = temp # temp를 text로
        new_hello_world.save() # 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # POST 요청에 의한 응답으로 text에 값을 보냄
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

