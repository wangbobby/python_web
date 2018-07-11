# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime
from blog import models

# Create your views here.

# user_list = []

def cur_time(request):
    times = datetime.datetime.now()

    # return HttpResponse("<h1>ok</h1>")
    return render(request, "cur_time.html", {"abc":times})

def userInfo(request):

    if request.method == "POST":
        u = request.POST.get("username", None)
        s = request.POST.get("sex", None)
        e = request.POST.get("email", None)
        # username = request.POST.get("submit", None)
        # user = {"username":username, "sex":sex, "email":email}
        # user_list.append(user)

        models.UserInfo.objects.create(
            username = u,
            sex = s,
            email = e,
        )

        user_list = models.UserInfo.objects.all()
        # return render(request, "index.html")
        return render(request, "index.html", {"user_list":user_list})

        print username
        print sex
        print email
    return render(request, "index.html")

def special_case_2003(request):
    return HttpResponse("2003")

def year_archieve(request, year):
    return HttpResponse(year + "year")

def month_archieve(request, year, month):
    return HttpResponse(year + "-" + month)

def day_archieve(request, year, month, day):
    return HttpResponse(year + "=" + month + "=" + day)

# def index(request, name):
#     return HttpResponse(name)

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")

        if username == "alex" and pwd == "123":
            return HttpResponse("Successful Access...")
    return render(request, "login.html")