__author__ = 'brian'

from django.conf.urls import url
from . import views
from datetime import datetime
from My_bots.forms import BootstrapAuthenticationForm


urlpatterns=[
    # /index/
    url(r'^$',views.index,name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'home/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

]
