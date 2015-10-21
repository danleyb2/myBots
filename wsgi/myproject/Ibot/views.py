from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

import requests
import json
from .config import CONFIG,ACCESS_TOKEN

# Create your views here.




class Ibot:
    API_URL = 'https://api.instagram.com/v1/'
    USER_INFO_URL = API_URL + 'users/'

    def __init__(self, token):
        self.TOKEN = token

    def get_req(self, url):
        parameters = {'access_token': self.TOKEN}
        return requests.get(url, params=parameters)


def index(request):
    bot = Ibot(ACCESS_TOKEN)
    # feed=bot.get_req(Ibot.API_URL+'self/feed').text

    feed = requests.get(
        'https://api.instagram.com/v1/users/self/feed?access_token='+ACCESS_TOKEN).text
    data = json.loads(feed)

    users=[]
    for i in data['data']:
        d=i['user']
        d['mid']=i['id']
        d['likes_count']=i['likes']['count']
        d['comments_count']=i['comments']['count']
        d['link']=i['images']['low_resolution']['url']
        users.append(d)

    context = {
        'posts':users
    }
    return render(request,'Ibot/index.html',context)


def like(request,media_id):
    furl = "https://api.instagram.com/v1/media/"+media_id+"/likes?access_token=" + ACCESS_TOKEN
    feed=requests.post(furl)
    return HttpResponseRedirect(reverse('index'))

