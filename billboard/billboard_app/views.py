from django.shortcuts import render,reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import BillBoard
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,"billboard_app/base.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return HttpResponseRedirect('http://127.0.0.1:8000/login/')
    else:
        form = UserCreationForm()
    return render(request,
        "registration/register.html",
        { "form": form }
    )