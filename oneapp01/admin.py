# coding=UTF-8
# - - coding：utf-8 - -
from django.contrib import admin
from models import *
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','Gender','IDType','IDNumber','Birthdate','VolunteerMobile','Email','ContactPerson','ContactPersonMobile','PoliticalStatusID','Major','FamilyAddress','VolunteerIntro']

class naunfengAdmin(admin.ModelAdmin):
    list_display = ['id','title','where','active']

class t_volunteerAdmin(admin.ModelAdmin):
    list_display = ['id','name','account','accountpassword','email','phone']


class t_voluntary_activityAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'time', 'numberpeople', 'content', 'image_link','shortcontent','servicerequirement','contactpeople','contactphone','closingtime','activitycode']


class t_parents_child_campaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'time', 'numberpeople','contactname','contactphone', 'content', 'image_link']


class t_ask_helpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_num', 'id_num', 'key_word', 'content','state']


class t_donateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'when', 'goods', 'help_content', 'phone_num']


class t_charity_bazaarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'goods', 'phone_num', 'content', 'image_link']

class postcardAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','takepicturetime','linkimage','postcardnumber','jumplink']

class VoluntaryTeachingAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'time', 'numberpeople', 'content', 'image_link', 'shortcontent',
                    'servicerequirement', 'contactpeople', 'contactphone', 'closingtime', 'activitycode']


admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(naunfeng,naunfengAdmin)
admin.site.register(t_volunteer,t_volunteerAdmin)
admin.site.register(t_voluntary_activity,t_voluntary_activityAdmin)
admin.site.register(t_parents_child_campaign,t_parents_child_campaignAdmin)
admin.site.register(t_ask_help,t_ask_helpAdmin)
admin.site.register(t_donate,t_donateAdmin)
admin.site.register(t_charity_bazaar,t_charity_bazaarAdmin)
admin.site.register(postcard,postcardAdmin)
admin.site.register(VoluntaryTeaching,VoluntaryTeachingAdmin)