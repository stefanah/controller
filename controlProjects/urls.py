from django.conf.urls import patterns, include, url
from django.contrib import admin
from controlProjects import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Goal_Light_Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^GoalLight/', views.goalLight, name='GoalLight'),
    url(r'^goalLightRaw/', views.goalLightRaw, name='rawLight'),
   )
