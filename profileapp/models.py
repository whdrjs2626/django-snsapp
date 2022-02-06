from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 연결된 User 객체가 없어질 때(on_delete) Profile 객체도 없어지도록(CASCADE)
    # related_name을 설정하면 어떤 한 Profile과 연결된 user의 Profile을 가져올 때 user.profile로 가져올 수 있다.
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)