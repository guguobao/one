# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from oneapp01.models import UserInfo, t_voluntary_activity, postcard, t_parents_child_campaign, VoluntaryTeaching, agribusinesstyping,updatafood ,foodclass ,classname, classfirstfood
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.
#HttpRequset
def index(request):
    #get post cards message
    b = postcard.objects.all()[:9]      #下面的语句返回前面9 个对象(LIMIT 5)：
    a = len(b)
    #get active message
    activemessage = t_voluntary_activity.objects.all()[:4]
    activelen = len(activemessage)
    active = {}
    for i in range(activelen):
        list = {'shortcontent':activemessage[i].shortcontent,'numberpeople':activemessage[i].numberpeople,'image_link':activemessage[i].image_link}
        active[i] = list

    # get VoluntaryTeaching message
    VoluntaryTeachingmessage = VoluntaryTeaching.objects.all()[:3]
    VoluntaryTeachinglen = len(VoluntaryTeachingmessage)
    voluntaryteaching = {}
    for i in range(VoluntaryTeachinglen):
        list = {'shortcontent': VoluntaryTeachingmessage[i].shortcontent, 'image_link': VoluntaryTeachingmessage[i].image_link}
        voluntaryteaching[i] = list

    # get t_parents_child_campaign message
    parents_childmessage = t_parents_child_campaign.objects.all()[:2]
    parents_childlen = len(parents_childmessage)
    parents_child = {}
    for i in range(parents_childlen):
        list = {'shortcontent':parents_childmessage[i].shortcontent,'image_link':parents_childmessage[i].image_link}
        parents_child[i] = list


    c = {}
    d = {'displaytwo':'none','display':'block'}
    for i in range(0,a,1):
        list = {'name':b[i].name,'takepicturetime':b[i].takepicturetime,'linkimage':b[i].linkimage,'price':b[i].price,'jumplink':b[i].jumplink,}
        c[i]=list
    c['d']=d
    c['active'] = active
    c['parents_child'] = parents_child
    c['voluntaryteaching'] = voluntaryteaching

    return render(request,'one/default.html',c)
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
              'servicerequirement':b.servicerequirement,'image_link':b.image_link}

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


#get 分类表单
def getclassname():
    classnames = classname.objects.all()
    list = []
    for i in range(len(classnames)):
        str = classnames[i].classnames.encode("utf-8")
        list.append(str)
    return list

#get

#农商
def agribusiness(request):
   # list={'#TopAds':'#TopAds','/TopAds':'/TopAds','#KeyWords':'#KeyWords','/KeyWords':'/KeyWords','#equal IsImportant true':'#equal IsImportant true','else':'else','/equal':'/equal'}
    #get agribusinesstyping  all  object
    typing = agribusinesstyping.objects.all()
    typinglen = len(typing)
    typinglist = []
   #get all typing
    for i in range(typinglen):
        list = []
        typingname = typing[i].typingfood
        list = typingname.split(u"、")
        typinglist.append(list)#不能用typinglist[i] = ...
    typinglink = []
    #get all link of typing
    for i in range(typinglen):
        list = []
        typingname = typing[i].typinglink
        list = typingname.split(u"、")
        typinglink.append(list)
    test = []

    # get new updatafoods
    allfoods = updatafood.objects.all().values("id")
    lenth = len(allfoods)
    if lenth < 4:
        lenth=4
    updatafoods = updatafood.objects.all()[lenth-4:lenth]
    agribusiness = {}
    newsfood = []


    for i in range(4):
        list = {'name':updatafoods[i].name,'jumplink':updatafoods[i].jumplink,'image_link':updatafoods[i].image_link,'shortcontent':updatafoods[i].shortcontent,'content':updatafoods[i].content}
        newsfood.append(list)
    #agribusiness['newsfood'] = newsfood


    for i in range(typinglen):
        b = []
        for j in range(len(typinglink[i])):
            a = {'food':typinglist[i][j],'link':typinglink[i][j]}
            b.append(a)
        test.append(b)

    
    typingall = []
    for i in range(typinglen):
        list = {'name':typing[i].name,'image_link':typing[i].image_link,'typingfood':test[i],'typinglink':typinglink[i]}
        typingall.append(list)
       
    #get classfood
    classfoods = foodclass.objects.all()
    foodslen = len(classfoods)
    classfoodlist = []
    classlist = getclassname()
    for i in  range(foodslen):
        index = classfoods[i].classname
        list = {'id':classfoods[i].id,'classname':classlist[index]}
        classfoodlist.append(list)




    lists = {'typingall':typingall,'newsfood':newsfood,'classfoodlist':classfoodlist}

    return render(request,'one/agribusiness.html',lists)

#农商2
def agribusinesschild(request):

    a = request.GET['number']
    a = int(a)
    if request.method == 'GET':
        classfoods = foodclass.objects.all()
        classfirstfoods = classfirstfood.objects.all()
        updatafoods = updatafood.objects.all()
        getclassfood = classfoods[a-1]
        index= [getclassfood.foods1.id,getclassfood.foods2.id,getclassfood.foods3.id,getclassfood.foods4.id,getclassfood.foods5.id,getclassfood.foods6.id,getclassfood.firstfood.id]
        foodslist = {}
        for i in range(6):
            list = {'image_link':updatafoods[index[i]-1].image_link,'name':updatafoods[index[i]-1].name}
            foodslist[i] = list
        firstfood ={'imagelink':classfirstfoods[index[6]-1].imagelink,'name':classfirstfoods[index[6]-1].name}

        lists = {'foodslist':foodslist,'firstfood':firstfood}

        return render(request,'one/agribusiness001.html',lists)
        #return HttpResponse("504")
    else:
        return HttpResponse("404")

        # if a == '001':
        #     return render(request,'one/agribusiness001.html')
        # elif a == '002':
        #     return render(request, 'one/agribusiness002.html')
        # elif a == '003':
        #     return render(request, 'one/agribusiness003.html')
        # elif a == '004':
        #     return  render(request,'one/agribusiness004.html')
        # elif a == '005':
        #     return render(request, 'one/agribusiness005.html')
        # else:
        #     return HttpResponse("404")

#农商商品
def agribusinesspay(request):
    a = request.GET['name']
    if request.method == 'GET':
        return render(request,'one/agribusinesspay.html')

#亲子活动
def freebuy(request):
    # parents_childmessage = t_parents_child_campaign.objects.all()[:2]
    # name = request.GET['name']
    # # for i in parents_childmessage:
    # i = parents_childmessage[0]
    # if name == 'county':
    #     list = {'shortcontent':i.shortcontent,'image_link':i.image_link}

    if request.method == 'GET':
        # a = request.GET['name']
        return render(request,'one/freebuy.html')


def getclassname():
    classnames = classname.objects.all()
    list = []
    for i in range(len(classnames)):
        list.append(classnames[i].classnames)
    return list
