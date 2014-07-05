from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Goal_Light_Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
)
