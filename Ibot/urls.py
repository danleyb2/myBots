__author__ = 'brian'

from . import views
from django.conf.urls import url,patterns
from datetime import datetime

urlpatterns=[
    # /polls/
    url(r'^$',views.index,name='index'),
    url(r'^like',views.like,name='like'),


]
