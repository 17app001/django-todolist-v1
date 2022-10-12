from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def user_register(request):
    # 產生使用者表單
    form = UserCreationForm()
    message=''
       
    # 檢查是get or post
    if request.method=='GET':
        print('GET')
    elif request.method=='POST':
        print('POST')     
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 註冊功能
        # 密碼不能少於8各字元
        # 兩次密碼是否相同        
        # 使用者名稱不能重複
        # 進行註冊
        if len(password1)<8:
            message='密碼少於8各字元'
        elif password1!=password2:
            message='兩次密碼不同'
        else:
            if User.objects.filter(username=username).exists():
                message='帳號重複'
            else:
                User.objects.create_user(username=username,password=password1).save()
                message='註冊成功!'     
        

    return render(request,'./user/register.html',{'form' : form,'message':message})