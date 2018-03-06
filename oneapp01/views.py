# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from oneapp01.models import UserInfo, t_voluntary_activity
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.
#HttpRequset
def index(request):
    return render(request,'one/default.html',{'displaytwo':'none','display':'block'} )
#active page
def active(request):
    a=request.GET['a']
    try:
        b = t_voluntary_activity.objects.get(activitycode=a)
    except:
        return HttpResponse("404")
    else:
        list={'place':b.place,'releasetime':b.time,'closetime':b.closingtime,'shortcontent':b.shortcontent,
             'numberpeople':b.numberpeople,'content':b.content,'contactphone':b.contactphone,'contactpeople':b.contactpeople,
              'servicerequirement':b.servicerequirement,'picture':b.image_link}

    return render(request,'one/active .html',list)
#login
@csrf_exempt
def login(request):
    username_get = request.POST['name']
    password_get = request.POST['password']
    b=[]
    a = 0
    b = UserInfo.objects.filter(username=username_get)
    a = len(b)
    if a==0:
        return HttpResponse("0")
    else:
        if request.method == 'POST':
            #return  HttpResponse(result)
            if b[0].password==password_get:
                return render(request,'one/default.html',{'display':'none','displaytwo':'block','username':username_get} )
            else:
                return HttpResponse("0")

def register(request):
        return render(request,'one/register.html')

def adduser(request):
    if request.method == 'POST':
        LastName=request.POST['LastName']
        FirstName=request.POST['FirstName']
        Kpwd=request.POST['Kpwd']
        Kcpwd=request.POST['Kcpwd']
        IDType= request.POST['IDType']
        IDNumber=request.POST['IDNumber']
        Birthdate=request.POST['Birthdate']
        VolunteerMobile=request.POST['VolunteerMobile']
        Email=request.POST['Email']
        Gender=request.POST['Gender']
        ContactPerson=request.POST['ContactPerson']
        ContactPersonMobile=request.POST['ContactPersonMobile']
        PoliticalStatusID=request.POST['PoliticalStatusID']
        Major=request.POST['Major']
        FamilyAddress=request.POST['FamilyAddress']
        VolunteerIntro=request.POST['VolunteerIntro']

        userinfo=UserInfo()
        username_get=LastName+FirstName
        b=[]
        a = 0
        b = UserInfo.objects.filter(username=username_get)
        a = len(b)
        if a==0:
            userinfo.username=username_get
            userinfo.Birthdate=Birthdate
            if Kpwd==Kcpwd:
                userinfo.password=Kcpwd
            userinfo.ContactPerson=ContactPerson
            userinfo.Email=Email
            if Gender=='1':
                userinfo.Gender='男'
            elif Gender=='2':
                userinfo.Gender='女'
            userinfo.FamilyAddress=FamilyAddress
            userinfo.IDNumber=IDNumber
            if IDType=='1':
                userinfo.IDType='身份证'
            else:
                userinfo.IDType='其他'
            userinfo.ContactPersonMobile=ContactPersonMobile
            if PoliticalStatusID=='1':
                userinfo.PoliticalStatusID='共产党'
            else:
                userinfo.PoliticalStatusID='其他'
            userinfo.Major=Major
            userinfo.VolunteerIntro=VolunteerIntro
            userinfo.VolunteerMobile=VolunteerMobile

            userinfo.save()
            return HttpResponse("ok")
        else:
            return HttpResponse(u"用户已存在")

#关于我们，就是帮助页面
def helphtml(request):
    return render(request,'one/help.html')

#农商
def agribusiness(request):
   # list={'#TopAds':'#TopAds','/TopAds':'/TopAds','#KeyWords':'#KeyWords','/KeyWords':'/KeyWords','#equal IsImportant true':'#equal IsImportant true','else':'else','/equal':'/equal'}
    return render(request,'one/agribusiness.html')

#农商2
def agribusinesschild(request):
   # return render(request, 'one/agribusiness001.html')
    a = request.GET['number']
    if request.method == 'GET':

        if a == '001':
            return render(request,'one/agribusiness001.html')
        elif a == '002':
            return render(request, 'one/agribusiness002.html')
        elif a == '003':
            return render(request, 'one/agribusiness003.html')
        elif a == '004':
            return  render(request,'one/agribusiness004.html')
        elif a == '005':
            return render(request, 'one/agribusiness005.html')
        else:
            return HttpResponse("404")

#农商商品
def agribusinesspay(request):
    a = request.GET['name']
    if request.method == 'GET':
        return render(request,'one/agribusinesspay.html')
