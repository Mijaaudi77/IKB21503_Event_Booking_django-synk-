from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from auditlog.models import AuditLog
import uuid

def get_client_ip(request):
    """Get client IP address"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def booking_list(request):
    """Display all bookings for current user"""
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    """Create a new booking"""
    if request.method == 'POST':
        # Get form data with input validation
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        
        # Input validation
        if not title:
            messages.error(request, 'Title is required.')
            return render(request, 'bookings/create.html')
        
        if not date:
            messages.error(request, 'Date is required.')
            return render(request, 'bookings/create.html')
        
        # Create the booking
        try:
            booking = Booking.objects.create(
                user=request.user,
                title=title,
                description=description,
                date=date,
                time=time if time else None
            )
            
            # Log the action (if auditlog is available)
            try:
                AuditLog.objects.create(
                    user=request.user,
                    action='CREATE',
                    ip_address=get_client_ip(request),
                    user_agent=request.META.get('HTTP_USER_AGENT', ''),
                    details=f"Created booking: {booking.title}"
                )
            except:
                pass  # Skip if auditlog fails
            
            messages.success(request, f'Booking "{title}" created successfully!')
            return redirect('booking_list')
            
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            return render(request, 'bookings/create.html')
    
    # GET request - show empty form
    return render(request, 'bookings/create.html')

@login_required
def booking_detail(request, booking_id):
    """View booking details"""
    try:
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        return render(request, 'bookings/detail.html', {'booking': booking})
    except (ValueError, Booking.DoesNotExist):
        messages.error(request, 'Booking not found or access denied.')
        return redirect('booking_list')

@login_required
def booking_update(request, booking_id):
    """Update existing booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title', booking.title).strip()
        description = request.POST.get('description', booking.description).strip()
        date = request.POST.get('date', booking.date)
        time = request.POST.get('time', booking.time)
        
        # Update booking
        booking.title = title
        booking.description = description
        booking.date = date
        booking.time = time if time else None
        booking.save()
        
        # Log update
        try:
            AuditLog.objects.create(
                user=request.user,
                action='UPDATE',
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                details=f"Updated booking: {booking.title}"
            )
        except:
            pass
        
        messages.success(request, f'Booking "{title}" updated successfully!')
        return redirect('booking_detail', booking_id=booking.id)
    
    # GET request - show form with current data
    return render(request, 'bookings/update.html', {'booking': booking})

@login_required
def booking_delete(request, booking_id):
    """Delete booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        title = booking.title
        booking.delete()
        
        # Log deletion
        try:
            AuditLog.objects.create(
                user=request.user,
                action='DELETE',
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                details=f"Deleted booking: {title}"
            )
        except:
            pass
        
        messages.success(request, f'Booking "{title}" deleted successfully!')
        return redirect('booking_list')
    
    # GET request - show confirmation
    return render(request, 'bookings/delete.html', {'booking': booking})