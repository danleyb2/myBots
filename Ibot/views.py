
from django.shortcuts import render, get_object_or_404


import urllib
import json
# Create your views here.

'''
index display last posted pic owners with their likes count

like last number posted pics and return name of those liked
schedule likes

'''

def index(request):
    return render(request,'Ibot/index.html')

def like(request):
    ACCESS_TOKEN='446256538.cfb70db.5aeebfad6ad1400898b1ddef9a70466e'
    furl="https://api.instagram.com/v1/users/self/feed?access_token="+ACCESS_TOKEN
    response=urllib.urlopen(furl)
    data=response.read()
    pass
