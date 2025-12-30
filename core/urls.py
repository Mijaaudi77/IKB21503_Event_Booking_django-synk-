from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Include app URLs
    path('accounts/', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
    path('auditlog/', include('auditlog.urls')),
    
    # Home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# For development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)