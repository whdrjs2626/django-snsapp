from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView  # 지정한 뷰 함수 가져오기

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 경로 지정
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
]
