from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [ 
    # ex: /home/
    # url(r'^$', views.home, name = 'home'),
    url(r'^create/', views.create,name='createuser'),
    url(r'^signin/', views.signin,name='signin'),
    url(r'^createSkill/', views.createSkill,name='createskill'),
    url(r'^getSkill/', views.getSkill,name='getskill'),
    url(r'^search/', views.search,name='search'),
    url(r'^(?P<username>\w+)', views.userdata, name='lookupuser'),
]
