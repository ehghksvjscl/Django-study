from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# https://github.com/django/django/blob/master/django/contrib/auth/forms.py
class SignupForm(UserCreationForm):
    # UserCreationForm에서 email field가 필수 값 변경 및 확인
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields['email'].required)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    # UserCreationForm definition
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","email","first_name","last_name"]

    # email field validationCheck
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 입니다.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','website_url','bio','phone_number','bio']
