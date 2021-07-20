from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from unitest import models
from django.template import  RequestContext
# from index.views import loginFilter


def index(request):
    return HttpResponse("<title>unit_index</title><h1>Hello, world. You're at the unitest index.</h1>")

def showAll(request):

    user_list = models.userinfo.objects.all()

    return render(request, 'unitest/showAll.html',{'user_list':user_list})

def toaddUser(request):

    return render(request, 'unitest/addUser.html')

def addUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        memo = request.POST['memo']
        models.userinfo.objects.create(name=name,email=email,memo=memo)
    return  HttpResponseRedirect('showAll')

def toUpdate(request):
    print(request)
    context={}
    full_path = request.get_full_path()
    id = full_path.split("/")[-1]
    print(id)
    user = models.userinfo.objects.filter(id=id)[0]
    context['user']=user

    return render(request, 'unitest/updateUser.html',context)

def updateUser(request):
    print(request)
    full_path = request.get_full_path()
    id = full_path.split("/")[-1]
    print(id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        memo = request.POST['memo']
        id = request.POST['id']
        models.userinfo.objects.filter(id=id).update(name=name,email=email,memo=memo)
    return HttpResponseRedirect('showAll')



def deleteUser(request):
    print(request)
    full_path = request.get_full_path()
    id = full_path.split("/")[-1]
    print(id)
    # 删除
    models.userinfo.objects.filter(id=id).delete()
    return  HttpResponseRedirect('../showAll')

