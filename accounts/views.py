from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Handle AuditLog gracefully
try:
    from auditlog.models import AuditLog
    AUDITLOG_ENABLED = True
except (ImportError, Exception):
    AUDITLOG_ENABLED = False
    print("Note: AuditLog not available, continuing without audit logging")

def get_client_ip(request):
    """Get client IP address for logging"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                
                # Try to log registration if auditlog is available
                if AUDITLOG_ENABLED:
                    try:
                        AuditLog.objects.create(
                            user=user,
                            action='CREATE',
                            ip_address=get_client_ip(request),
                            user_agent=request.META.get('HTTP_USER_AGENT', ''),
                            details=f"User registered: {user.username}"
                        )
                    except:
                        pass  # Skip if auditlog fails
                
                # Auto login after registration
                login(request, user)
                messages.success(request, 'Registration successful! Welcome.')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Registration error: {str(e)}')
                print(f"Registration error: {e}")
        else:
            # Show field-specific errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """Handle user login"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Try to log login if auditlog is available
                if AUDITLOG_ENABLED:
                    try:
                        AuditLog.objects.create(
                            user=user,
                            action='LOGIN',
                            ip_address=get_client_ip(request),
                            user_agent=request.META.get('HTTP_USER_AGENT', ''),
                            details=f"User logged in: {user.username}"
                        )
                    except:
                        pass
                
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """Handle user logout"""
    if AUDITLOG_ENABLED and request.user.is_authenticated:
        try:
            AuditLog.objects.create(
                user=request.user,
                action='LOGOUT',
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                details=f"User logged out: {request.user.username}"
            )
        except:
            pass
    
    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    """Display user profile"""
    return render(request, 'accounts/profile.html', {'user': request.user})

