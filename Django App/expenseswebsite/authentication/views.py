from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib import auth

print(User)
# Create your views here.
class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({"username_error":'username already in use'},status=409)
        return JsonResponse({'email_valid': True})
    
class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphabetic characters'},status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error":'username already in use'},status=409)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,'Password too short')
                    return render(request,'authentication/register.html',context)
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_staff = True
                
                
                user.save()
                
                messages.success(request,'Account Created Successfully!')
                return redirect('login')
            return render(request,'authentication/login.html')

class VerificationView(View):
    def get(self,request):
        try:
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
        except Exception as ex:
            pass
        return redirect('login')


class LoginView(View):
     def get(self, request):
        return render(request, 'authentication/login.html')
     def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('expenses')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')
        # messages.success(request,'Successfully Registered')
        # messages.warning(request,'Warning')
        # messages.info(request,'Info')
        # messages.error(request,'Error!!')
 

        # return render(request,'authentication/register.html')
