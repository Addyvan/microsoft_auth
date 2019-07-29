from django.contrib import admin
from django.urls import path, include
from microsoft_auth import views

urlpatterns = [
    path('microsoft_auth/', include('microsoft_auth.urls')),
    path('admin/', admin.site.urls),
]