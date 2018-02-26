#coding:utf-8
from django.conf.urls import url
import views
urlpatterns=[
   url('^index/$',views.index),
   url('^active/$',views.active),
   url('^login/$',views.login,name='login'),
   url('^register/$',views.register,name='register'),
   url('^register/add/$',views.adduser,name='adduser'),
   url('^help/$',views.helphtml,name='helphtml')
   #


]