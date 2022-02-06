
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) # 요청을 받으면서 pk를 가진 User
        if not profile.user == request.user: # 해당 profile의 user가 요청의 user와 같지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated