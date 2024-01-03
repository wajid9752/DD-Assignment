
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("account.urls",namespace="account")),
    path('', include("employee.urls",namespace="employee")),
    path('', include("admins.urls",namespace="admins")),
    path('', include("manager.urls",namespace="manager")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
