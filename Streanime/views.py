from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests_html import HTMLSession
import os
import googleapiclient.discovery
from django.shortcuts import render
import urllib.request
import json

f = open('episodes.json',)
eplist = json.load(f)
n=1

def home(request):
    
    ep = eplist['episodesl1'][0]['0']  # url
    return render(request, "home.html", {'no': n, 'eplink': ep})


def search(request):
    if 'episode' in request.GET:
        n = request.GET['episode']
        nu = int(n)-1
        num = str(nu)
        ep = eplist['episodesl1'][0][num]
    
    return render(request, "episode.html", {'no': n, 'eplink': ep})
    


def nextep(request,no):
    nu = no-1
    print(nu)
    num = str(nu)
    ep = eplist['episodesl1'][0][num]
    return render(request, "nextep.html", {'no': no, 'eplink': ep})
    