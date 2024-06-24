from django.shortcuts import render,redirect
from .models import ResultModel
from django.contrib.auth import logout




# Create your views here.

def indexPage(request):
    return render(request,'index.html')



def resultPage(request,studentname):
    student=ResultModel.objects.get(studentname=studentname)
    return render(request,'results.html',{'student':student})


def checkview(request):
    studentname=request.POST['studentname']
    email=request.POST['email']
    sid=request.POST['sid']
    
    if ResultModel.objects.filter(studentname=studentname,email=email,studentID=sid).exists():
        return redirect('/'+studentname+'/?email='+email)
    else:
        return render(request,'index.html')
    
    
    
    
def logoutPage(request):
    logout(request)
    
    return redirect('logout')