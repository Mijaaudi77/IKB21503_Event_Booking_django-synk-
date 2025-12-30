from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AuditLog

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def audit_log_list(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'auditlog/logs.html', {'logs': logs})

@login_required
@user_passes_test(is_admin)
def audit_log_detail(request, log_id):
    log = get_object_or_404(AuditLog, id=log_id)
    return render(request, 'auditlog/detail.html', {'log': log})