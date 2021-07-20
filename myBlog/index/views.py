from django.shortcuts import render
from index.models import logindata,user
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.
from django.http import HttpResponse



def index(request):
    return  render(request, 'index/index.html')


def toLogin(request,message=""):
    context_dict = {"message":message}
    if request.session.get('haslogin',False)==True:
        return index(request)
    return  render(request, 'index/login.html', context_dict)


def logined(request):
    context_dict = {}
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print(email,pwd)
    if pwd==None or email==None or pwd =="" or email=="":
        return toLogin(request,message="Please enter valid username and password!!")
    else:
        if loginfailed(email,pwd):
            return toLogin(request,message="username or password error!!")
        else:
            print("request.session.keys() ",request.session.keys())
            request.session['haslogin']=True

            # request.session['name']="Makers"
            print("getUserName(email) ",getUserName(email))
            request.session['name']=getUserName(email)
            return render(request, 'index/index.html', context_dict)


def loginfailed(email, pwd):
    # user = logindata.objects.filter(email=email)
    user = logindata.objects.get(email=email)
    print(type(user))
    # print(user.values("pwd")[0]['pwd'])
    print("user pwd ", user.pwd)
    # if user.values("pwd")[0]['pwd']==pwd:
    if user.pwd == pwd:
        return False
    else:
        return True


def toRegister(request,message=""):
    if message=="":
        message = "welcome to the register page!!"
    context_dict =  {"message":message}
    return  render(request, 'index/register.html', context_dict)



def checkRegister(request,message=""):
    queryKey = request.POST.get("key")

    print("queryKey==> ",queryKey)


    if queryKey=="name":
        username = request.POST.get("username")
        print("username ==> ", username)
        if username=="":
            data = {'queryKey': "username 不能为空！！！"}
            return JsonResponse(data)
        if len(user.objects.filter(name = username))==0:
            data = {'queryKey': ""}
            return JsonResponse(data)
        else:
            data = {'queryKey': "username 已存在！！！"}
            return JsonResponse(data)


    if queryKey=="email":
        email = request.POST.get("email")
        print("email ==> ", email)
        if email=="":
            data = {'queryKey': "email 不能为空！！！"}
            return JsonResponse(data)
        if len(user.objects.filter(email = email))==0:
            data = {'queryKey': ""}
            return JsonResponse(data)
        else:
            data = {'queryKey': "email 已存在！！！"}
            return JsonResponse(data)


    data = { 'queryKey': str(queryKey)}
    return JsonResponse(data)



def registerUser(request,message=""):

    name = request.POST.get("username")
    email =  request.POST.get("email")
    age = request.POST.get("age")
    pwd = request.POST.get("pwd")

    if len(user.objects.filter(name=name)) != 0 \
        or len(user.objects.filter(email = email))!=0:
        message = "注册失败！！！"
        return  toRegister(request,message=message)

    u = user(name=name,age=age,email=email)
    logd  = logindata(email=email,pwd=pwd)
    u.save()
    logd.save()

    return  HttpResponseRedirect("toLogin")


def Logout(request):
    del request.session['haslogin']
    # return render(request, 'index/index.html')
    return HttpResponseRedirect('../index')


def getUserName(email):
    print("user.objects.filter(email=email).valuesname ",user.objects.filter(email=email).values("name"))
    print("user--name: ",user.objects.get(email=email).name)
    # return user.objects.filter(email=email).values("name")[0]['name']
    return user.objects.get(email=email).name

# def loginFilter(request):
#     if request.session.get('haslogin', False) == False:
#         return HttpResponseRedirect('/index/toLogin')
#     else:
#         print(request.get_full_path())
#         if request.get_full_path()=='/':
#             return HttpResponseRedirect('/index')
#         else:
#             return HttpResponseRedirect(request.get_full_path())




