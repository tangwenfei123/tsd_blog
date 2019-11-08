import datetime as datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog import models
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    article = models.Article.objects.all()
    # 现在的时间
    now = datetime.datetime.now()
    content = {
        "article":article,
        "now":now

    }
    return  render(request, "index.html",content)

def login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清理数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username = data['username'],password=data['password'])
            if user:
                login(request,user)
                return redirect("blog:index")
            else:
                return  HttpResponse("账号密码有误！请重新输入。")
        else:
            return HttpResponse("账号密码输入不合法！")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        content = {
            'form':user_login_form
        }
        return render(request,'index.html',content)
    else:
        return HttpResponse("请使用合法请求！！！")







def article(request):
    pass

def loginout(request):
    loginout(request)
    return  redirect("blog:index")


def words(request):
    pass



