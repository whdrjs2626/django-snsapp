from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, \
    AccountDeleteView  # 지정한 뷰 함수 가져오기

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 경로 지정
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # detail은 특정 유저의 정보를 봐야 함 - 계정의 ID(pk)가 필요함, <int:pk> - pk라는 이름의 int 정보를 받겠다.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
