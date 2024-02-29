from typing import Tuple

from django.shortcuts import render, redirect
from buzzapp.models import Member
from buzzapp.models import Contact
from buzzapp.models import Users


# Create your views here.

def index(request):
    if request.method == 'POST':

        contact = Contact(name=request.POST['name'],
                          email=request.POST['email'],
                          subject=request.POST['subject'],
                          message=request.POST['message']
                          )
        contact.save()
        return redirect('/')

    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':

        member = Member(username=request.POST['username'], email=request.POST['email address'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def Portfolio(request):
    return render(request, 'portfolio-details.html')


def upload(request):
    return render(request, 'upload.html')
def detail(request):
    details = Contact.objects.all()
    return render(request,'details.html',{'details':details})





def user(request):
    users = Users.objects.all()
    return render(request,'User-details.html',{'users':users})

def adminhome(request):
   if request.method == 'POST':
       if Member.objects.filter(username = request.POST['username'],password=request.POST['password']).exists():
           member= Member.objects.get(username=request.POST['username'],password=request.POST['password'])

           return  render(request,'adminhome.html',{ 'member' : member})
       else:
           return render(request,'login.html')

   else:
       return render(request,'login.html')

