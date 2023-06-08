from django.shortcuts import render
from django.http import HttpResponse
from .models import Adminlog,Userdata

def welcome(request):
    return render(request,'index.html')

def sb(request):
    s='welcome to SB college'
    return render(request,'sbcollege.html',{'wel':s})

def logadmin(request):
    return render(request,'adminhome.html')

def UserRegistration(request):
    return render(request,'userreg.html')

def UserData(request):
    if request.method =='POST':
        n=request.POST['name']
        un=request.POST['uname']
        pwd=request.POST['pwd']
        a=request.POST['age']
        e=request.POST['email']
    db= Userdata(name=n,uname=un,password=pwd,age=a,email=e)
    db.save()
    return render(request, 'adminhome.html')

def checkadmin(request):
    if request.method == 'POST':
        t=request.POST['utype']
        if t=='ad':
            u=request.POST['uname']
            p=request.POST['pwd']
            d=Adminlog.objects.get(uname=u)
            d1=d.uname
            if u==d.uname:
                if p==d.password:
                    return render(request, 'sbcollege.html', {'wel':d1})
                else:
                    return HttpResponse('Incorrect password')
            else:
                return HttpResponse('Invalid user')
        elif t=='us':
            u = request.POST['uname']
            p = request.POST['pwd']
            d = Userdata.objects.get(uname=u)
            d1 = d.name
            if u == d.uname:
                if p == d.password:
                    return render(request, 'sbcollege.html', {'wel':d1})
                else:
                    return HttpResponse('Incorrect password')
            else:
                return HttpResponse('Invalid user')