from django.http import JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *  
from django.http import JsonResponse 
# Create your views here.

def home(request):
    form=StudentRegistration()
    stud=User.objects.all()
    return render(request,'studentinfo/home.html',{'form':form,'stud':stud})

def save_data(request):
    if request.method=="POST":
        form=StudentRegistration(request.POST)
        if form.is_valid():
            sid=request.POST.get('sid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if(sid==''):
                usr=User(name = name,email = email,password = password)
            else:
                usr=User(id=sid,name = name,email = email,password = password)
            usr.save() 
            std=User.objects.values()
            student_data=list(std)
            
            return JsonResponse({'status':1,'student_data':student_data})
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})

def edit_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        stu=User.objects.get(pk=id)
        stu_data={"id":stu.id,"name":stu.name,"email":stu.email,"password":stu.password}
        return JsonResponse(stu_data)
        