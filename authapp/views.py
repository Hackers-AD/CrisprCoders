from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class LoginView(View):
    errors = []


    def get(self, request):
        return render(request, 'auth/login.html', {'errors': self.errors,})

    def post(self, request):
        self.errors = []
        username = None
        password = None

        if request.POST.get('username', ""):
            username = request.POST['username']
        if request.POST.get('password', ""):
            password = request.POST['password']

        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        self.errors.append("Provided credentials doesn't match any records in database")
        
        return self.get(request)

class RegisterView(View):
    errors = []
    full_name = '' 
    email = ''
    username = None

    def get(self, request):
        return render(request, 'auth/register.html', {'errors': self.errors,
                                'full_name': self.full_name, 'email': self.email, 'username':self.username})

    def post(self, request):
        self.errors = []
        new_password = None
        confirm_password = None

        if request.POST.get('full_name', ""):
            self.full_name = request.POST['full_name']
        if request.POST.get('email', ""):
            self.email = request.POST['email']

        self.username = request.POST['username']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password != confirm_password:
            self.errors.append("New password and confirmed password didn't match")
        if  len(new_password) < 8:
            self.errors.append("Password length must be 8 or greater")

        unique_user = User.objects.filter(username = self.username )
        if len(unique_user) > 0:
            self.errors.append("Username already taken.")

        if len(self.errors) == 0:
            user = User.objects.create_user(username=self.username, password=new_password, email=self.email, 
                first_name=self.full_name, is_staff=True)
            return redirect('/')

        return self.get(request)

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('/') 
