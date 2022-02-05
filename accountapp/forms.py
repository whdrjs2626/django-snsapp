from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm): # UpdateView(정보수정) 전용 폼 / UserCreationForm을 상속받음
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 상속 받은 그대로 사용함
        self.fields['username'].disabled = True # ID 입력 칸만 비활성화 시킴 - 회원정보 수정 시 ID는 변경하지 않게 하기 위함