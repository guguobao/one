# coding:utf-8
from django.db import models


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
    image_link=models.CharField(max_length=25,default='img')
    activitycode=models.IntegerField(default='000')

    # def __unicode__(self):
    #     return self.content.encode('gbk')

#t_parents and child campaign
class t_parents_child_campaign(models.Model):
    place=models.CharField(max_length=50,default='place')
    time=models.DateField()
    numberpeople=models.IntegerField(default='0')
    content=models.CharField(max_length=150,default='content')
    contactname=models.CharField(max_length=150,default='childred parents')
    contactphone=models.IntegerField(default='112223333')
    image_link=models.CharField(max_length=25,default='img')

    def __unicode__(self):
        return self.content.encode('utf-8')

#people ask help
class t_ask_help(models.Model):
    name=models.CharField(max_length=20,default='name')
    phone_num=models.IntegerField(default='13433618211')
    id_num=models.IntegerField(default='000')
    key_word=models.CharField(max_length=50,default='关键字')
    content=models.CharField(max_length=150,default='content')
    state=models.BooleanField(default=False)
    def __unicode__(self):
        return self.content.encode('utf-8')

#people donate thing
class t_donate(models.Model):
    name=models.CharField(max_length=20,default='mane')
    phone_num=models.IntegerField(default='13345457487')
    help_content=models.CharField(max_length=150,default='help message')
    goods=models.CharField(max_length=50,default='help thing')
    when=models.CharField(max_length=25,default='time')

    def __unicode__(self):
        return self.help_content.encode('utf-8')

#charity bazaar
class t_charity_bazaar(models.Model):
    goods=models.CharField(max_length=50,default='goods')
    name=models.CharField(max_length=20,default='name')
    phone_num=models.IntegerField(default='1343668954')
    content=models.CharField(max_length=150,default='content')
    image_link=models.CharField(max_length=25,default='img')

    def __unicode__(self):
        return self.content.encode('utf-8')



