from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): # 모델 폼을 사용
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']