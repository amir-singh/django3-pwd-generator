from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return HttpResponse("Hello AMir SINGH")
def eggs(request):
    return HttpResponse("<h1>Eggs are good for health</h1>")
def home1(request):
    return render(request,'generator/home.html',{'password' : 'asdsadspnkgkbn22'})
def about(request):
    return render(request,'generator/aboutus.html')

def password(request):
    thepassword =''
    chs=list("abcdefghijklmnopqrstuvwxyz")
    #length=10
    length=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        chs.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        chs.extend(list("!@#$%&"))
    if request.GET.get('numbers'):
        chs.extend(list("1234567890"))

    for x in range(length):
        thepassword += random.choice(chs)
    return render(request,'generator/password.html',{'passwordu' : thepassword })
