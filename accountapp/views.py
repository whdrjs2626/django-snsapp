from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'}) # 첫번쨰 인자는 request, 두번째는 템플릿 명
        # POST 요청에 의한 응답으로 text에 값을 보냄
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})

