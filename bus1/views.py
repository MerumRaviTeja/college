from django.shortcuts import render,redirect
from .models import faculty,student
from .forms import facultyform,studentform,facultyloginform,studentloginform
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
def facultyreg(request):
    f=facultyform()
    if request.method=='POST':
        f=facultyform(request.POST)
        if f.is_valid():
            to=f.cleaned_data['email']
            facultyname=f.cleaned_data['faculty_name']
            
            return redirect(mailsending1,to,facultyname)
          
    else:
        return render(request,'bus1/registration.html',{'f':f})
def studentreg(request):
    f=studentform()
    if request.method=='POST':
        f=studentform(request.POST)
        if f.is_valid():
            f.save()
            to=f.cleaned_data['email']
            sid=student.objects.filter(email=to)
            for i in sid:
                  studentid=i.student_id
                  studentname=i.student_name
            return redirect(mailsending,to,studentid,studentname)
    else:
        return render(request,'bus1/registration1.html',{'f':f})
def facultylogin(request):
    if request.method=='POST':
        lform=facultyloginform(request.POST)
        if lform.is_valid():
            user_name=request.POST.get('subject','')
            Password=request.POST.get('email','')
            user1=faculty.objects.filter(subject=user_name)
            pwd1=faculty.objects.filter(email=Password)
            if  user1 and pwd1:
                             return HttpResponse("Ok Done")
            else:
                return HttpResponse('invalied')
        else:
                logform=facultyloginform()
                return render(request,'bus1/login.html',{'form':logform})
    else:
        logform=facultyloginform()
        return render(request,'bus1/login.html', {'form':logform})
def studentlogin(request):
    if request.method=='POST':
        lform=studentloginform(request.POST)
        if lform.is_valid():
            user_name=request.POST.get('student_ID','')
            Password=request.POST.get('branch','')
            user1=student.objects.filter(student_id=user_name)
            pwd1=student.objects.filter(branch=Password)
            if  user1 and pwd1:
                             return HttpResponse("ok")
            else:
                return HttpResponse('invalied')
        else:
                logform=studentloginform()
                return render(request,'bus1/login.html',{'form':logform})
    else:
        logform=studentloginform()
        return render(request,'bus1/login.html', {'form':logform})
def mailsending(request,to,studentid,studentname):
    From="leningeddam017@gmail.com"

    To=to
  
    Sub="Dear "+studentname
    Message="Your Student_ID is "+studentid
    try:
               
                mail = EmailMessage(Sub,From,Message,[To])
                mail.send()
                return render(request,'bus1/u.html',{'name':studentname})
    except:
                return HttpResponse("Oops something happen")
def mailsending1(request,to,facultyname):
    From="leningeddam017@gmail.com"

    To=to
  
    Sub="Dear "+facultyname
    Message="Your successfuly register"
    try:
               
                mail = EmailMessage(Sub,From,Message,[To])
                mail.send()
                return render(request,'bus1/u1.html',{'name':facultyname})
    except:
                return HttpResponse("Oops something happen")
