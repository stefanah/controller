from django.conf.urls import patterns, include, url
from login import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#    url(r'^about/$', views.about, name='about'),
#    url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
#    url(r'^add_category/$', views.add_category, name='add_category'),
#    url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^theLogin/$', views.user_login, name='theLogin'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^user_logout/', views.user_logout, name='logout'),
    )
