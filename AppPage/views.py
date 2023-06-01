from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

class NewItemForm(forms.Form):
    item = forms.IntegerField(label='Number of items')

def index(request):
    
    if "AppPage" not in request.session:

        request.session["AppPage"] = []

    return render(request, "AppPage/index.html" , {"AppPage": request.session["AppPage"]})

def add(request):
    if request.method == "POST":
        form=NewItemForm(request.POST)

        if form.is_valid():

            item=form.cleaned_data["item"]

            request.session["AppPage"]+=[item]

            return HttpResponseRedirect(reverse("AppPage:index"))
        else:
            return render(request, "AppPage/add.html" , {})
        
    return render(request, "AppPage/add.html" , {"form": NewItemForm()})

