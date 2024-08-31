from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import User 

# API View for User Registration
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

# HTML View for User Registration
class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse_lazy('user_list'))

        return render(request, 'register.html', {'error': 'All fields are required.'})

# HTML View for Listing Users
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

