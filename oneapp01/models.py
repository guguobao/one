# coding:utf-8
from django.db import models
#from oneapp01.views import getclassname

#def decode(info):
#    return info.decode('utf-8')
# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=20,default='your name')
    password=models.CharField(max_length=20,default='your password')
    Gender=models.CharField(max_length=20,default='1')
    IDType=models.CharField(max_length=20,default='1')
    IDNumber=models.IntegerField(default='440981')
    Birthdate=models.CharField(max_length=100,default='your birthDay')
    VolunteerMobile=models.CharField(max_length=150,default='your phone')
    Email=models.CharField(max_length=100,default='your email')
    ContactPerson=models.CharField(max_length=100,default='contact name')
    ContactPersonMobile=models.IntegerField(default='12345678901')
    PoliticalStatusID=models.CharField(max_length=25,default='1')
    Major=models.CharField(max_length=100,default='计算机科学与技术')
    FamilyAddress=models.CharField(max_length=200,default="addrend")
    VolunteerIntro=models.CharField(max_length=500,default="intro")
    #
    # def __unicode__(self):
    #     return self.username.encode('unicode')


class naunfeng(models.Model):
    title=models.CharField(max_length=50,default='title')
    where=models.CharField(max_length=50,default='where')
    time=models.DateField()
    active=models.BooleanField(default=True)

#volunteer message table
class t_volunteer(models.Model):
    account=models.CharField(max_length=20,default='account')
    accountpassword=models.CharField(max_length=25,default='password')
    name=models.CharField(max_length=20,default='name')
    phone=models.CharField(max_length=25,default='phone')
    email=models.CharField(max_length=25,default='email')

    def __unicode__(self):
        return self.name.encode('utf-8')

#volunteer activity message table
class t_voluntary_activity(models.Model):
    place=models.CharField(max_length=100,default='place')
    time=models.DateField()
    closingtime=models.DateField()
    numberpeople=models.IntegerField(default='0')
    shortcontent=models.CharField(max_length=100,default='shortcontent')
    content=models.CharField(max_length=250,default='content')
    contactphone=models.IntegerField(default='0')
    servicerequirement = models.CharField(max_length=50,default='要求')
    contactpeople=models.CharField(max_length=25,default='name')
    image_link=models.CharField(max_length=100,default='picture/.jpg')
    activitycode=models.IntegerField(default='000')

    # def __unicode__(self):
    #     return self.content.encode('gbk')

#t_parents and child campaign
class t_parents_child_campaign(models.Model):
    place=models.CharField(max_length=50,default='place')
    time=models.DateField()
    numberpeople=models.IntegerField(default='0')
    shortcontent=models.CharField(max_length=100,default='shortcontent')
    content=models.CharField(max_length=150,default='content')
    contactname=models.CharField(max_length=150,default='childred parents')
    contactphone=models.IntegerField(default='112223333')
    image_link=models.CharField(max_length=100,default='picture/.jpg')

#people ask help
class t_ask_help(models.Model):
    name=models.CharField(max_length=20,default='name')
    phone_num=models.IntegerField(default='13433618211')
    id_num=models.IntegerField(default='000')
    key_word=models.CharField(max_length=50,default='关键字')
    content=models.CharField(max_length=150,default='content')
    state=models.BooleanField(default=False)

#people donate thing
class t_donate(models.Model):
    name=models.CharField(max_length=20,default='mane')
    phone_num=models.IntegerField(default='13345457487')
    help_content=models.CharField(max_length=150,default='help message')
    goods=models.CharField(max_length=50,default='help thing')
    when=models.CharField(max_length=25,default='time')


#charity bazaar
class t_charity_bazaar(models.Model):
    goods=models.CharField(max_length=50,default='goods')
    name=models.CharField(max_length=20,default='name')
    phone_num=models.IntegerField(default='1343668954')
    content=models.CharField(max_length=150,default='content')
    image_link=models.CharField(max_length=25,default='img')

    # def __unicode__(self):
    #     return self.content.encode('utf-8')
#postcard
class postcard(models.Model):
    name=models.CharField(max_length=100,default='postcard')
    price=models.CharField(max_length=50,default='price')
    takepicturetime=models.DateField()
    linkimage=models.CharField(max_length=100,default='postcord/picture/.jpg')
    postcardnumber=models.IntegerField(max_length=25,default='001')
    jumplink=models.CharField(max_length=1000,default='')

#义教
class VoluntaryTeaching(models.Model):
    place = models.CharField(max_length=100, default='地点')
    time = models.DateField()
    closingtime = models.DateField()
    numberpeople = models.IntegerField(default='0')
    shortcontent = models.CharField(max_length=100, default='简介')
    content = models.CharField(max_length=250, default='内容')
    contactphone = models.IntegerField(default='0')
    servicerequirement = models.CharField(max_length=50, default='要求')
    contactpeople = models.CharField(max_length=25, default='name')
    image_link = models.CharField(max_length=100, default='picture/.jpg')
    activitycode = models.IntegerField(default='000')

#农商分类
class agribusinesstyping(models.Model):
    name = models.CharField(max_length=100,default='分类一')
    image_link =  models.CharField(max_length=200,default='picture/agribusinesstyping/logo.png')
    typingfood = models.CharField(max_length=200,default='分类请用、分隔符')
    typinglink = models.CharField(max_length=100,default='每个分类链接用、分割符')


#农商商品最新产品
class updatafood(models.Model):
    name = models.CharField(max_length=200,default='')
    jumplink = models.CharField(max_length=200,default='')
    image_link = models.CharField(max_length=300,default='agribusiness/picture/updatafoodpicture/agribusinesstyping/logo.png')
    shortcontent = models.CharField(max_length=300,default='shortcontent')
    content = models.CharField(max_length=200,default='content')
    price = models.CharField(max_length=300,null=True,blank=True,default='')

    def __unicode__(self):
        return u' %s %s %s %s %s %s %s %s %s %s %s %s' % ("name:",self.name,"__image_link:",self.image_link,"__jumplink:",self.jumplink,"__content:", self.content,"__shortcontent:",self.shortcontent,"__price:",self.price)


class classname(models.Model):
    classnames = models.CharField(max_length=100,default="分类一")

def getclassname():
    classnames = classname.objects.all()
    list = []
    for i in range(len(classnames)):
        str = classnames[i].classnames.encode("utf-8")
        list.append(str)
    return list


#农商商品分类汇
class foodclass(models.Model):
    list = getclassname()
    choicelist = []
    string =  ","
    str = ()
    for i in range(len(list)):
        str = (i,list[i])
        choicelist.append(str)
   #str2 = string.join(choicelist)
    #classnamelist = ((1, list[0]), (2, list[1]), (3, '分类三'), (4, '分类四'),)
    classnamelist = (choicelist)
    classname = models.IntegerField(choices=classnamelist,default=1)
    foods1 = models.ForeignKey('updatafood',related_name='foods1')
    foods2 = models.ForeignKey('updatafood',related_name='foods2')
    foods3 = models.ForeignKey('updatafood',related_name='foods3')
    foods4 = models.ForeignKey('updatafood',related_name='foods4')
    foods5 = models.ForeignKey('updatafood',related_name='foods5')
    foods6 = models.ForeignKey('updatafood',related_name='foods6')
    firstfood = models.ForeignKey('classfirstfood',related_name='firstfood')


class classfirstfood(models.Model):
    name = models.CharField(max_length=100,default='')
    imagelink = models.CharField(max_length=200,default='agribusiness/picture/updatafoodpicture/agribusinesstyping/logo.png')
    shortcontent = models.CharField(max_length=200,default='')
    content = models.CharField(max_length=300,default='')

    def __unicode__(self):
        return u"%s %s %s %s %s %s %s %s" %('name:',self.name,'imagelink',self.imagelink,'shortcontent',self.shortcontent,'content',self.content)




