from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:detail') # detail페이지로 리다이렉션 하려해도 갈 수 없다 - pk값을 필요로 하기 때문 - get_success_url 함수로 해결
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # profile form엔 user를 정하지 않는다. 이를 자동으로 설정해주기 위한 함수
        temp_profile = form.save(commit=False) # form에 작성한 내용을 임시(commit=false)로 저장
        temp_profile.user = self.request.user # 현재 요청의 user를 임시 profile 객체의 user로 설정
        temp_profile.save() # 실제로 저장
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk}) # 성공 시 detail 페이지로 리다이렉트하되 pk값을 전송

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'