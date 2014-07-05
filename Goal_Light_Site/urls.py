from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Goal_Light_Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^controlProjects/', include('controlProjects.urls')),
)
