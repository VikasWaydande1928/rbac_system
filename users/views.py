from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response  # Importing Response
from .permissions import IsAdmin, IsModerator, IsUser  # Ensure these permissions are correctly defined
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser  # or User model if you're using the default

def register(request):
    if request.method == "POST":
        # Handle the registration logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # You can add validation and user creation logic here
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'message': 'User logged in successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.http import JsonResponse

def logout(request):
    # Log the user out
    auth_logout(request)
    return JsonResponse({'message': 'User logged out successfully'}, status=200)
# Admin only view
@api_view(['GET'])
@permission_classes([IsAdmin])
def admin_only_view(request):
    return Response({"message": "Welcome, Admin!"})

# Moderator only view
@api_view(['GET'])
@permission_classes([IsModerator])
def moderator_only_view(request):
    return Response({"message": "Welcome, Moderator!"})

# User only view
@api_view(['GET'])
@permission_classes([IsUser])
def user_only_view(request):
    return Response({"message": "Welcome, User!"})
