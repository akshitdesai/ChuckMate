from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
import requests


joke = ""
username1 = "Chuck"
username2 = "Norris"
newreq = 'https://api.chucknorris.io/jokes/random'

def about(request):
    return render(request,'about.html')

def home(request):
    joke = str(requests.get(newreq).json()['value']) 
    if username1 != "Chuck" or username2 != "Norris":
        joke = joke.replace("Chuck",username1)
        joke = joke.replace("Norris",username2)
    return render(request,'home.html',{ "joke":joke })

def reset(request):
    global username1,username2
    username1 = "Chuck"
    username2 = "Norris"
    joke = str(requests.get(newreq).json()['value']) 
    return render(request,'home.html',{ "joke":joke })
    
def custom(request):
    submitbutton= request.POST.get("submit")
    form= UserForm(request.POST or None)
    global username1,username2
    if form.is_valid():
        username1= form.cleaned_data.get("first_name")
        username2= form.cleaned_data.get("last_name")
        return HttpResponseRedirect('/')
    context= {'form': form, 'firstname': username1, 'lastname':username2,'submitbutton': submitbutton}
    return render(request, 'custom.html', context)