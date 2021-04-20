from django.shortcuts import render,redirect
from NoteApp.forms import UsForm,ComplaintForm,ImForm,UtupForm,ChPwdForm
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from NoteApp.models import ImProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(request,'html/register.html',{'u':p})
@login_required

def dashboard(request):
	return render(request,'html/dashboard.html')


def profile(request):
	return render(request,'html/profile.html')

def Books(request):
	return render(request,'html/Books.html')

def complaint(request):
	if request.method=="POST":
		data=ComplaintForm(request.POST)
		if data.is_valid():
			subject='Confirmation_Complaint'
			body="Successfully_complainted by "+request.POST['p_name']
			receiver=request.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(request,"Successfully sent complaint" )
			return redirect('/')
	form=ComplaintForm()
	return render(request,'html/complaint.html',{'p':form})

'''def complaint(request):
	if request.method=="POST":
		subject=request.POST['p_subject']
		body=request.POST['p_body']
		receiver=request.POST['p_email']
		sender=settings.EMAIL_HOST_USER
		send_mail(subject,body,sender,[receiver])
		messages.success(request,"Successfully sent complaint ")
		return redirect('/')
	form=ComplaintForm()
	return render(request,'html/complaint.html',{'p':form})'''
def updpf(request):
	if request.method=="POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/updateprofile.html',{'us':u,'imp':i})
@login_required


def cgf(request):
	if request.method=="POST":
		c=ChPwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lgo')
	c=ChPwdForm(user=request)
	return render(request,'html/changepassword.html',{'p':c})