import requests
from django.contrib.sites import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse
import urllib.request

from django.views.decorators.csrf import csrf_exempt



from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.
from requests import Response
from rest_framework.views import APIView
from selenium import webdriver
import json


def events(request):
    ik = []
    title = []
    img = []
    link = []
    author = []
    datetime = []
    kk = 0
    driver = webdriver.Chrome("/home/amank/Development/insight_api/chromedriver")
    driver.get("http://otakukart.com/animeblog/")
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, "lxml")
    for div in soup.findAll("div", attrs={"class": "td-module-thumb"}):
        ik.append(kk)
        link.append(div.find("a")["href"])
        title.append(div.find("a")["title"])
        img.append(div.find("img")["src"])
        kk = kk + 1
    for span in soup.findAll("span", attrs={"class": "td-post-author-name"}):
        author.append(span.text)
    for span in soup.findAll("span", attrs={"class": "td-post-date"}):
        datetime.append(span.find("time")["datetime"])

    total = []
    for i in ik:
        total.append(
            {"title": title[i], "url": link[i], "img_url": img[i], "author": author[i], "datetime": datetime[i]})

    str_json = str(total)
    str_dict_json = str_json
    s=str_dict_json.replace("'", '"')

    return HttpResponse(s)










