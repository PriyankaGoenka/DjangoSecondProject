from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.

def home(request):
    return HttpResponse("Hello Candidates!! Welcome to Djanjo Training!")

#def form_view(request):
   # if request.method=="POST":
    #    form=forms.Login(request.POST)
     #   if form.is_valid():
       #    try:
         #      form.save()
       #        return redirect('success') 
        #   except:
         #       print("Error saving")
           
            
  #  form=forms.Login
   # return render(request,'SecondP/login.html',{'form':form})
def create(request):
    if request.method=="POST":
        form=forms.SignIn(request.POST)
        if form.is_valid():
           try:
               form.save()
               return redirect('success') 
           except:
                print("Error saving")
    else:        
        form=forms.SignIn()
    return render(request,'SecondP/login.html',{'form':form})

def success(request):
    return render(request, "SecondP/success.html")

#def create1(request):
#    if request.method=="POST":
#        form1=forms.Signup(request.POST)
#        if form1.is_valid():
#           try:
#               form1.save()
#               return redirect('Loginn') 
#           except:
#                print("Error saving")
#    else:        
#        form1=forms.Signup()
#    return render(request,'SecondP/Signup.html',{'form1':form1})

#def create2(request):
#    if request.method=="POST":
#        form2=forms.Loginn(request.POST)
#        if form2.is_valid():
#           try:
#               form2.save()
#               return redirect('show') 
#           except:
#                print("Error saving")
#    else:        
#        form2=forms.Loginn()
#    return render(request,'SecondP/Loginn.html',{'form2':form2})

#def Login(request):
  # return render(request, "SecondP/Login.html")

#def show(request):
 #   Loginn=Loginn.objects.all()
  #  return render(request, "SecondP/show.html",{'Loginn':Loginn} )


