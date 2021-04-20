from django.urls import path
from NoteApp import views #from . import views
from django.contrib.auth import views as ad
 

urlpatterns = [
    path('',views.home,name="hm"),
    path('pro/',views.profile,name='profile'),
    path('cp/',views.complaint,name='complaint'),
    path('Books/',views.Books,name='Books'),
    path('abt/',views.about,name="at"),
    path('cnt/',views.contact,name="ct"),
    path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name="log"),
    path('rg/',views.regi,name="rg"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('updf/',views.updpf,name="upf"),
    path('ch/',views.cgf,name="cg"),
    path('rst/',ad.PasswordResetView.as_view(template_name="html/resetpass.html"),name="reset_password"),
    path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html/resetpassworddone.html'),name='password_reset_done'),
    path('rst_confirm/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html/resetconfirm.html'),name='password_reset_confirm'),

]