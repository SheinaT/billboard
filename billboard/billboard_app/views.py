from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Billboard
from .forms import PostForm
from django.utils import timezone
import datetime
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# def welcome(request):
#     request.COOKIES.get('last_visited')
#     response = render(request, 'billboard_app/logged_in.html')
#     response.set_cookie('last_visited', 'visited before')
#     return response

def index(request):
    post_list= Billboard.objects.order_by('pub_date')
    if request.method== "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            # post.author= request.user
            # post.pub_date=timezone.now()
            # post.save()
            # return HttpResponseRedirect('billboard_app/loggedin.html')
    else:
        form=PostForm(initial={'pub_date':datetime.datetime.now()})

    context= {
        'post_list': Billboard.objects.order_by('pub_date'),
        'form':form
    }
    print(context, form)
    return render(request,"billboard_app/loggedin.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request,
        "registration/register.html",
        { "form": form }
    )
