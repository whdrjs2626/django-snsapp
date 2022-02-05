from django.urls import path

from accountapp.views import hello_world # 지정한 뷰 함수 가져오기

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 경로 지정
]
