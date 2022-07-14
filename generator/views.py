from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password' : 'h12312312'})

def password(request):

    characters = list('abcdefjhijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGJHKLMNOPQRSTUVXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = request.GET.get('length',12)
    length = int(length)

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def page_not_found(request):
    return render(request, 'generator/page_not_found.html')

def about(request):
    return render(request, 'generator/about.html')

def contacts(request):
    return render(request, 'generator/contacts.html')

def logout(request):
    return render(request, 'generator/logout.html',{'username' : 'hello'})

def sendmail(request):

    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    message = request.GET.get('message')

    return render(request, 'generator/sendmail.html', {'firstname' : firstname})

