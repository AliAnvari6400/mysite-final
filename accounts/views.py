from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from django.urls import is_valid_path
from accounts.forms import UserCreationForm,ResetForm,ChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages


# Create your views here.
def login_view(request):
    next_url = request.GET.get('next', '/')
    if not request.user.is_authenticated:
        # if request.method == 'POST':
            if request.method == 'POST':
                userinput = request.POST['username']
                try:
                    username = User.objects.get(email=userinput).username
                except User.DoesNotExist:
                    username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    next_url = request.POST.get('next') #, next_url)
                    parsed_url = urlparse(next_url)
                    if not parsed_url.netloc and is_valid_path(next_url):
                        return HttpResponseRedirect(next_url)
                else:
                    messages.add_message(request,messages.ERROR,"incorrect username or password. please try again")
            form = AuthenticationForm()
            context = {'form':form,'next':next_url}
            return render(request,'accounts/login2.html',context)
    else:
        return redirect('/')
    

@login_required(login_url='/')  
def logout_view(request):
    next_url = request.GET.get('next', '/')
    logout(request)
    parsed_url = urlparse(next_url)
    if not parsed_url.netloc and is_valid_path(next_url):
        return HttpResponseRedirect(next_url)
    #return redirect('/')
    
    
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,"Your registeration completed")
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,"Enter correct password and email")
                return redirect('/')
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/login2.html',context)
    else:
        return redirect('/')
   
    
key_dict={}
def keygenerator(x):
        key = random.randint(1000,100000)
        key_dict[x]= key
        return key

def reset_view(request):
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            key = keygenerator(email)
            print(email,key)
            subject = "Reset Password"
            message = "please follow this link to change password: http://127.0.0.1:8000/accounts/change/?email="+str(email)+"&key="+str(key)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False,)
            messages.add_message(request,messages.SUCCESS,"email sent for reset password")
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,"your email not exist")
            return redirect('/')
      
    form = ResetForm()
    context = {'form':form}
    return render(request,'accounts/reset2.html',context)

def change_view(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        key = request.GET.get('key')
        valid_key = key_dict[email]
        if key == str(valid_key):
            form = ChangeForm()
            context = {'form':form,'email':email,'key':key}
            return render(request,'accounts/change2.html',context)
        else: 
            messages.add_message(request,messages.ERROR,"get a link for reset password again")
            return redirect('/')  
                
    if request.method == 'POST':
            form = ChangeForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                key = form.cleaned_data['key']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                print(key_dict[email])
                if str(key) == str(key_dict[email]):
                    while password1 == password2:
                        user = User.objects.filter(email=email)[0]
                        user.set_password(password1)
                        user.save()
                        # -------- send email -------
                        subject = "Change Password"
                        message = str(user)+",your password changed successfully"
                        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False,)
                        # ---------------------------
                        messages.add_message(request,messages.SUCCESS,"your password changed")
                        key_dict[email] = None
                        return redirect('/')
                    messages.add_message(request,messages.ERROR,"password not matched")
                else: 
                    messages.add_message(request,messages.ERROR,"get a link for reset password again")
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,"enter your password again")
    
