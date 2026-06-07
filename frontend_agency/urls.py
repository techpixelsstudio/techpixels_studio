from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Main Navigation Links
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career'),

    # Blog System
    path('blog/', views.blog, name='blog'),
    path('blog/all/', views.all_blogs, name='all_blogs'), # Navin Route
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # Dedicated Services Links
    path('services/web-development/', views.web_dev, name='web_dev'),
    path('services/app-development/', views.app_dev, name='app_dev'),
    path('services/seo-optimization/', views.seo, name='seo'),
    path('services/video-editing/', views.video_editing, name='video_editing'),
    path('services/cloud-hosting/', views.cloud_hosting, name='cloud_hosting'),
    path('services/custom-tech/', views.custom_tech, name='custom_tech'),
    path('services/digital-marketing/', views.digital_marketing, name='digital_marketing'),

    # Subscribe logic
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)