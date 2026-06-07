from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Fkt ekda include karaycha ahe
    path('', include('frontend_agency.urls')),
]