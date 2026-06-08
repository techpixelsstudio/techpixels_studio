from django.db import models
from django.utils.text import slugify

# 1. Contact Form (Lead Generation) Database
class ContactLead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True, null=True)
    service_type = models.CharField(max_length=50, blank=True, null=True)
    budget = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead: {self.name} | Needs: {self.service_type}"

# 2. Dynamic Job Openings
class JobOpening(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., Senior Backend Architect")
    tag1 = models.CharField(max_length=100, help_text="e.g., PYTHON / DJANGO")
    tag2 = models.CharField(max_length=100, help_text="e.g., FULL-TIME")
    tag3 = models.CharField(max_length=100, help_text="e.g., REMOTE")
    description = models.TextField(help_text="Job details here...")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 3. Form submit jhalyavar data aani resume save karnyasaathi
class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    portfolio = models.URLField(blank=True, null=True)
    short_note = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.role}"

# 4. Blog Posts
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# 5. Instagram Reels
class InstagramReel(models.Model):
    reel_url = models.URLField(help_text="Instagram Reel chi link (e.g., https://www.instagram.com/reel/...)")
    thumbnail = models.ImageField(upload_to='reels_thumbnails/', help_text="Reel cha cover photo")
    views = models.CharField(max_length=20, default="10.5K", help_text="e.g., 15.2K")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reel - {self.views} Views"