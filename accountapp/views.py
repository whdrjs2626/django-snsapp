from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

has_ownership = [account_ownership_required, login_required] # decorater 배열

@login_required # 로그인 인증 decorator - 함수형 뷰 전용
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')  # POST 요청의 폼에서 hello_world_input인 데이터를 가져와라

        new_hello_world = HelloWorld()  # HelloWorld 객체(모델) 생성
        new_hello_world.text = temp  # temp를 text로
        new_hello_world.save()  # 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # POST 요청에 의한 응답으로 text에 값을 보냄
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})




class AccountCreateView(CreateView): # Create
    model = User # 장고에서 제공하는 User 객체
    form_class = UserCreationForm # 폼
    success_url = reverse_lazy('accountapp:hello_world') # 이 계정을 만드는데 성공했을 경우 돌아갈 url
    template_name = 'accountapp/create.html' # 회원가입 프론트

class AccountDetailView(DetailView): # Read - Detail
    model = User
    context_object_name = 'target_user' # detail 페이지에서 user의 정보를 출력하면 무조건 나의 정보만 띄운다. 즉 다른 사람의 페이지로 들어가도 내정보가 나옴 / 따라서 이렇게 target_user를 설정
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get') # 클래스형 뷰에 인증 decorator을 사용하기 위해서 method_decorator를 사용해야 함
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView): # Update - Create와 똑같다.
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm # Update 전용 폼으로 사용
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'