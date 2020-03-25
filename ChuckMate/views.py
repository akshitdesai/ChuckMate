from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
import requests,requests_oauthlib
import random

joke = ""
newreq = 'https://api.chucknorris.io/jokes/random?category='
cat = ["animal","career","celebrity","dev","fashion",
"food","history","money","movie","music","political","religion","science","sport","travel"]

def about(request):
    return render(request,'about.html')

def home(request):
    if 'fname' not in request.session:
        request.session['fname'] = 'Chuck'
        request.session['lname'] = 'Norris'
        request.session['re'] = False
    fname = request.session.get('fname', 'Chuck')
    lname = request.session.get('lname', 'Norris')
    re = request.session.get('re', False)
    newcat = []
    if re is True:
        newcat.append("explicit")
    newcat.append(random.choice(cat))
    newcat.append(random.choice(cat))
    joke = str(requests.get(newreq+str(random.choice(newcat))).json()['value']) 
    if fname != "Chuck" and lname != "Norris":
        joke = joke.replace("Chuck",fname)
        joke = joke.replace("CHUCK",fname.upper())
        joke = joke.replace("Norris",lname)
        joke = joke.replace("NORRIS",lname.upper())
    whats = joke +"%0a%0a Explore More Jokes on ChuckMate"
    whats += "%0a%0a http://chuckmate.pythonanywhere.com %0a%0a Enjoy and Spread Love❤️"
    return render(request,'index.html',{ "joke":joke,"whats":whats })
    
def custom(request):
    submitbutton= request.POST.get("submit")
    form= UserForm(request.POST or None)

    #global username
    if form.is_valid():
        request.session['fname'] = form.cleaned_data.get("fname").title()
        request.session['lname'] = form.cleaned_data.get("lname").title()
        request.session['re'] = form.cleaned_data.get('re')
        return HttpResponseRedirect('/')
    context= {'form': form, 'fname': request.session['fname'], 'lname': request.session['lname'],'submitbutton': submitbutton}
    return render(request, 'custom.html', context)