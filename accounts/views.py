from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import SignupForm, ProfileForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()

            # login Auth
            auth_login(request,signed_user)
            next_url = request.GET.get("next",'/') 

            messages.success(request,"회원가입 환영합니다.")
            signed_user.send_welcome_email() # FIXME: Celery로 처리하는 것을 추천
            return redirect(next_url)
    else :
        form = SignupForm()
    
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })

# ref = https://github.com/django/django/blob/main/django/contrib/auth/views.py
login = LoginView.as_view(template_name="accounts/login_form.html")

# ref = https://github.com/django/django/blob/main/django/contrib/auth/views.py
def logout(request):
    messages.success(request,'로그아웃 되었습니다.')
    return logout_then_login(request)

# proi
@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=request.user) # instance = 초기 데이터\
        if form.is_valid():
            form.save()
            messages.success(request,'프로필을 수정/저장 했습니다.')
            return redirect("profile_edit")

    else:
        form = ProfileForm(instance=request.user)
    return render(request,'accounts/profile_edit_form.html',{
        "form":form
    })