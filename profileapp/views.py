from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # profile form엔 user를 정하지 않는다. 이를 자동으로 설정해주기 위한 함수
        temp_profile = form.save(commit=False) # form에 작성한 내용을 임시(commit=false)로 저장
        temp_profile.user = self.request.user # 현재 요청의 user를 임시 profile 객체의 user로 설정
        temp_profile.save() # 실제로 저장
        return super().form_valid(form)