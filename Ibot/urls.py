__author__ = 'brian'

from . import views
from django.conf.urls import url,patterns
from datetime import datetime

urlpatterns=[
    # /polls/
    url(r'^$',views.home,name='index'),
    url(r'^like',views.like,name='like'),
    url(r'^login/(\w*)',views.login,name='login'),


]
