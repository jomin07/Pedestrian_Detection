from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime

from .models import *
import os

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        reg=registerr(name=name,email=email,phone=phone,password=password)
        reg.save()
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif registerr.objects.filter(email=email,password=password).exists():
        userdetails=registerr.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
        
        return render(request,'index.html')
        
    else:
        return render(request, 'login.html', {'success':'Invalid email id or Password'})
        

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def v_users(request):
    user = registerr.objects.all()
    return render(request, 'viewusers.html', {'result': user})

def test(request):
    return render(request,'test.html')

def addimg(request):
    if request.method=="POST":
        u_id = request.session['uid']
        result = request.POST.get('result')
        image = request.FILES['image']
        try:
            os.remove("media/input/test.mp4")
        except:
            pass
        fs = FileSystemStorage(location="media/input")
        fs.save("test.mp4",image)
        os.system("python yolov5/detect.py --source media/input/test.mp4 --weights yolov5/yolov5s.pt")
        fs = FileSystemStorage()
        fs.save("test.mp4",image)
        cus=imagess(u_id=u_id,result=result,image=image.name)
        cus.save()
        return render(request,'index.html')
    
# def v_result(request):
#     uid=request.session['uid']
#     user = imagess.objects.filter(u_id=uid)
#     return render(request, 'viewresult.html', {'result': user})

def live(request):
    return render(request,'livecam.html')

def start_det(request):
    os.system("python yolov5/detect.py --source 0 --weights yolov5/yolov5s.pt")
    return render(request,'livecam.html')