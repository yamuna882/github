from django.shortcuts import render,redirect
from NoteApp.forms import UsForm,ComplaintForm,ImForm,UtupForm,ChPwdForm,Books_AvailForm,Books_AvailForm_admin,Expire_date
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from NoteApp.models import ImProfile,Books_Avail,st_admin_data
from django.contrib.auth.decorators import login_required
import sys

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
def Books_AvailF(rq):
	if rq.method=="POST":
		k=rq.POST['Book_count']
		a=rq.POST['Book_author']
		b=rq.POST['Book_name']
		notes=Books_Avail.objects.all()
		f=0
		for i in notes:
			if i.Book_name==b and i.Book_author==a:
				m=i.Book_count+int(k)
				i.Book_count=m
				i.Book_Updatedcount=i.Book_Updatedcount+int(k)
				i.save()
				f=1
		if f==0:
			e=Books_AvailForm_admin(rq.POST)
			if e.is_valid():
				q=e.save(commit=False)
				q.Book_Updatedcount=k
				q.up_id=rq.user.id
				q.save()
	e=Books_AvailForm_admin()
	e2=Books_Avail.objects.all()
	return render(rq,"html/Books_Avail.html",{'t':e2,'t1':e})
@login_required
def sendrequest(rq):
	if rq.method=="POST":
		a=rq.POST['Book_name']
		c=rq.POST['Book_author']

		b=rq.POST['browser']
		if b=='Book_Retrun':
			notes=st_admin_data.objects.filter(Book_name=a)
			for i in notes:
				if i.Book_author==c and i.issue_status==1:
					i.issue_status='3'
					i.save()
		else:
			print(a)
			book_name=[]
			e=Books_AvailForm(rq.POST)
			notes=Books_Avail.objects.all()
			for i in notes:
				if i.Book_name==a:
					k=i.Book_count
			print(book_name)

			if e.is_valid():
				q=e.save(commit=False)
				q.uid_id=rq.user.id
				q.Book_count=k
				q.save()

		
	e=Books_AvailForm()
	return render(rq,"html/sendrequest.html",{'t':e})
def studentbooks_avail(rq):
	e2=Books_Avail.objects.all()
	return render(rq,'html/studentbook_avail.html',{'t':e2})
@login_required
def myreq(req):
	notes=st_admin_data.objects.filter(uid_id=req.user.id)
	return render(req,'html/myres.html',{'data':notes})
def datadelete(req,id):
	obj=st_admin_data.objects.get(id=id)
	obj.delete()
	return redirect('/notipending')
def Bookdelete(req,id):
	obj=Books_Avail.objects.get(id=id)
	obj.delete()
	return redirect('/ba')

@login_required
def viewnt(req):
	accept=st_admin_data.objects.filter(issue_status=1).count()
	allnotes=st_admin_data.objects.all().count()
	re=st_admin_data.objects.filter(issue_status=2).count()
	return render(req,'html/adminpage.html',{'ac':accept,'all':allnotes,'a':re})
def notipending(req):
	pending2=st_admin_data.objects.all()
	data=Books_Avail.objects.filter()
	return render(req,'html/noti_pendingdata.html',{'p':pending2})
def rejecting(req):
	pending2=st_admin_data.objects.all()
	data=Books_Avail.objects.filter()
	return render(req,'html/noti_rejectingdata.html',{'p':pending2})

def accepting(req):
	pending2=st_admin_data.objects.all()
	data=Books_Avail.objects.filter()
	return render(req,'html/noti_acceptingdata.html',{'p':pending2})

def acceptadmin(req,id):
	if req.method=='POST':
		ac=st_admin_data.objects.get(id=id)
		a=req.POST.get('issue')
		b=req.POST.get('Expire')
		ac.Issue_date=a
		ac.Expire_date=b
		ac.save()
		return render(req,'html/expiredate.html')	
	else:
		ac=st_admin_data.objects.get(id=id)
		nam=ac.Book_name
		k=Books_Avail.objects.get(Book_name=nam)
		m=k.Book_count
		if m>0:
			m=m-1
			k.Book_count=m
			ac.Book_count=m
			ac.issue_status='1'
			ac.save()
			k.save()
			return render(req,'html/expiredate.html')
		else:
			ac.issue_status='2'
			ac.save()
		return redirect('/viewn')

def rejectadmin(req,id):
	rc=st_admin_data.objects.get(id=id)
	rc.issue_status='2'
	rc.save()
	return redirect('/viewn')

def books_return(request):
	rc=st_admin_data.objects.filter(issue_status=3)
	print(rc)
	return render(request,'html/Books_return.html',{'rc':rc})

def return_accept(rq,id):
	rc=st_admin_data.objects.get(id=id)
	rc.issue_status='4'
	rc.save()
	return redirect('books_return')







	

