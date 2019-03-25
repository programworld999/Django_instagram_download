from django.shortcuts import render
from django.http import HttpResponse

import re
import requests
from bs4 import BeautifulSoup
import urllib.request as DFU
#DFU (Download From URL)
import os
import random

# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    return render(request, "download/index.html", {})

def submit(request):
    url = request.GET['url']
    print(url)
    data = requests.get(url)
    str = data.text
    match = "data not found"
    match = re.findall(r'video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count', str)

    extraction = ".mp4"

    if len(match) == 0:
        match = re.findall(r'display_url\W\W\W([-\W\w]+)\W\W\Wdisplay_resources', str)
        extraction = ".jpg"


    context = {
        'src': match[0],
        'ext': extraction,
    }
    return render(request, "download/index.html", context)



def download(request):
    url = request.GET['url']
    ext = url[-3:-1]
    
    if (ext == "jp"):
        ext = ".jpg"
    else:
        ext = ".mp4"
    
    url = url[0: -4]

    uniqid = random.randint(0, 9)
    name = "sarjsk991" + str(uniqid)
    print(name)

    try:
        DFU.urlretrieve(url, name+ext)
        msg = "Download Successsful"
        msgType = "success"

    except:
        msg = "Sorry! Download Unsuccessful"
        msgType = "danger"

    context = {'msg': msg, 'msgType': msgType } 
    return render(request, 'download/index.html', context)

