import requests
from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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

from rest_framework.response import Response
from rest_framework.decorators import api_view

from events.forms import NameForm



@api_view()
def events(request, page_no):
    ik = []
    title = []
    img = []
    link = []
    author = []
    datetime = []
    kk = 0
    text =[]

    url="http://otakukart.com/animeblog/page/" + page_no + "/"

    driver = webdriver.PhantomJS(service_args=['--load-images=no'])
    #driver = webdriver.Chrome("home/amank/Development/insight_api/chromedriver")
    driver.get(url)
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, "lxml")
    for div in soup.findAll("div", attrs={"class": "td-module-thumb"}):
        ik.append(kk)
        link.append(div.find("a")["href"])
        title.append(div.find("a")["title"])
        img.append(div.find("img")["src"])
        kk = kk + 1
    for span in soup.findAll("span", attrs={"class": "td-post-author-name"}):
        author.append(str(span.text)[:-3])
    for span in soup.findAll("span", attrs={"class": "td-post-date"}):
        datetime.append(span.find("time")["datetime"])
    for div in soup.findAll("div",attrs={"class":"td-excerpt"}):
        text.append(div.text[1:])
    total = []
    for i in ik:
        total.append(
            {"title": title[i], "url": link[i], "img_url": img[i], "author": author[i],"text":text[i],"datetime": datetime[i]})

    return Response(total)
def event(request):
    return redirect(events, 1)


def testing(request):
    driver = webdriver.PhantomJS(service_args=['--load-images=no'])
    # driver = webdriver.Chrome("home/amank/Development/insight_api/chromedriver")
    driver.get("")
    html_source = driver.page_source
    return HttpResponse(html_source)

def get_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            page_no = form.cleaned_data['page_no']
            if page_no>660 or page_no<1:
                return HttpResponse("No content on this page please request again.")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect(events,page_no)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})