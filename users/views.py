from Demos.win32ts_logoff_disconnected import username
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from . import models  # importing models


# Create your views here.
def loginView(request):
    # # created models (data in database) . save is for saving in database
    # models.UserModel1(1,'Ravi','Ravi_honey7','ravi.sharon7@gmail.com',12345678).save()
    # # for updation
    # data=  models.UserModel1(2,'raghavi','Raghavi_honey3','raghavi.sharon@gmail.com',35246735)
    # data.save()
    # # for jumbling order
    # jumb=  models.UserModel1(3,name='honey',email='raghavi.sharon7@gmail.com',username='Raghavi_honey',password=67587986)
    # jumb.save()
    if request.method=="POST":
        username= request.POST['Username']
        password = request.POST['Password']
        models.UserModel1(username=username,password=password).save()
      #  models.UserModel1.objects.create(username=username,password=password)           # to create , need not save data will directly get updated

    return render(request,'Login.html')
def About(request):
    return render(request,'About.html')
def SignUp(request):
    if request.method=='POST':
        name=request.POST["name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        models.UserModel1(name=name,email=email,username=username,password=password).save()

    return render (request,'SignUp.html')
def Identify(request):
    return render(request,'Identify.html')
def Home(request):
    return render(request,'Home.html')
def Profile(request):
    #profile = models.UserModel1.objects.all()
    profile= models.UserModel1.objects.filter(name='Ravi')   #all is to get all data , # filter is to filter, filter returns list
    #profile=models.UserModel1.objects.get(name='Ravi')   # get is only to get unique values
    # print(profile)
    # for i in profile:
    #     print(i.sign ,i.name  +'|',i.username  +'|',i.email)

    for i in profile:
    #     i.email='ravi@email.com'             # to update code for filter and all
    #     i.save()
        i.delete()                             # to delete code for filter and all


    return render(request,'Profile.html',context={'name': profile})   # dic is passed to html (context data )

class UserView(View):     # here in brackets we gave view because we are converting this class into a view page
    def get(self,request):                   # here def is not function since its written in class it is now a method
        return render (request,'login.html')
    def post(self,request):
        return render(request, 'About.html')