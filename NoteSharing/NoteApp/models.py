from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import UniqueConstraint



# Create your models here.
class ComplaintBox(models.Model):
	p_name=models.CharField(max_length=120)
	p_email=models.EmailField(max_length=120)
	p_complaint=models.CharField(max_length=10000)

class st_admin_data(models.Model):
	Rg_No=models.CharField(max_length=120)
	Branch=models.CharField(max_length=120)
	Name=models.CharField(max_length=120)
	issue_status=models.IntegerField(default=0)
	Book_name=models.CharField(max_length=120)
	Book_author=models.CharField(max_length=120)
	Book_count=models.IntegerField(default=0)
	Issue_date=models.DateField(blank=True,null=True)
	Expire_date=models.DateField(blank=True,null=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

# @receiver(post_save,sender=User)
# def CreateProfile(sender,instance,created,**kwargs):
# 	if created:
# 		st_admin_data.objects.create(uid=instance)
	#p_subject=models.CharField(max_length=100)
	#p_body=models.CharField(max_length=1000)
class Books_Avail(models.Model):
	Book_name=models.CharField(max_length=120, unique=True)
	Book_author=models.CharField(max_length=120,default="")
	Book_count=models.IntegerField(default=0)
	Book_Updatedcount=models.IntegerField(default=0)	


@receiver(post_save,sender=User)
def CreateProfile(sender,instance,created,**kwargs):
	if created:
		Books_Avail.objects.create(up=instance)

class ImProfile(models.Model):
	g=[('M',"male"),('F',"female")]
	age=models.IntegerField(default=10)
	impf=models.ImageField(upload_to='profiles/',default="profile.jpg")
	gender=models.CharField(max_length=20,choices=g)
	uid=models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)
def CreateProfile(sender,instance,created,**kwargs):
	if created:
		ImProfile.objects.create(uid=instance)