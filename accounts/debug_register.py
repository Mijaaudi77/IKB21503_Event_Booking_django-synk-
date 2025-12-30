from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
import traceback

def debug_register_view(request):
    """Simple debug registration to identify the issue"""
    print("=== DEBUG REGISTRATION CALLED ===")
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        
        print(f"Form data: username={username}, password1={len(password1)} chars")
        
        # Basic validation
        errors = []
        
        if not username:
            errors.append("Username is required")
        
        if len(password1) < 8:
            errors.append("Password must be at least 8 characters")
        
        if password1 != password2:
            errors.append("Passwords do not match")
        
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists")
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'accounts/register.html')
        
        # Try to create user
        try:
            print("Creating user...")
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=request.POST.get('email', '')
            )
            print(f"User created: {user.username}")
            
            # Auto login
            login(request, user)
            print("User logged in")
            
            messages.success(request, f'Registration successful! Welcome {username}.')
            return redirect('home')
            
        except Exception as e:
            print(f"ERROR creating user: {e}")
            print(traceback.format_exc())
            messages.error(request, f'Registration failed: {str(e)}')
    
    # GET request
    return render(request, 'accounts/register.html')
