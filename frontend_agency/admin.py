from django.contrib import admin
from .models import ContactLead, JobApplication, JobOpening, BlogPost, InstagramReel

# ==========================================
# 1. CONTACT LEADS ADMIN 
# ==========================================
@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service_type')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('service_type',)

# ==========================================
# 2. DYNAMIC JOB OPENINGS ADMIN 
# ==========================================
@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag1', 'tag2', 'is_active', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_active',)

# ==========================================
# 3. JOB APPLICATIONS (WITH RESUME) ADMIN 
# ==========================================
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'applied_at')
    search_fields = ('full_name', 'email', 'role')
    list_filter = ('role',)



# (Baki che junye admin registers tasech thev...)

@admin.register(InstagramReel)
class InstagramReelAdmin(admin.ModelAdmin):
    list_display = ('reel_url', 'views', 'is_active', 'created_at')