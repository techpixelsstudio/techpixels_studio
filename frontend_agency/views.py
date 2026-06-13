from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .models import ContactLead, JobApplication, JobOpening, BlogPost, InstagramReel

# --- MAIN PAGES ---
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message', '')
        
        ContactLead.objects.create(
            name=name, phone=phone, email=email, message=message
        )
        
        subject = f"🚀 New Lead from HOMEPAGE: {name} | TechPixels"
        email_body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
        
        try:
            send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['techpixelsstudio@gmail.com'], fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e) 
        
        # Pop-up & Redirect to Home
        context = {
            'swal_trigger': True,
            'swal_msg': "Your inquiry has been submitted! Our senior architect will contact you shortly.",
            'redirect_url': '/'
        }
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company', 'Not Provided')
        service_type = request.POST.get('service_type', 'Not Provided')
        budget = request.POST.get('budget', 'Not Provided')
        message = request.POST.get('message', '')
        
        ContactLead.objects.create(
            name=name, phone=phone, email=email, company=company,
            service_type=service_type, budget=budget, message=message
        )
        
        subject = f"🚀 New Lead from ABOUT PAGE: {name} | TechPixels"
        email_body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nService Type: {service_type}\nMessage: {message}"
        
        try:
            send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['techpixelsstudio@gmail.com'], fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e)
        
        # Pop-up & Redirect to About
        context = {
            'swal_trigger': True,
            'swal_msg': "Tumacha msg amhala milala. Amhi lavkarch tumchyashi contact karu!",
            'redirect_url': '/about/'
        }
        return render(request, 'about.html', context)
        
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

# --- BLOG LOGIC ---
def blog(request):
    posts_without_slugs = BlogPost.objects.filter(slug='')
    for p in posts_without_slugs:
        p.save()

    posts = BlogPost.objects.all().order_by('-date_posted')[:6]
    reels = InstagramReel.objects.filter(is_active=True).order_by('-created_at')[:3]
    return render(request, 'blog.html', {'posts': posts, 'reels': reels})

def all_blogs(request):
    posts_without_slugs = BlogPost.objects.filter(slug='')
    for p in posts_without_slugs:
        p.save()

    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'all_blogs.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})

# --- SERVICES ---
def services(request):
    return render(request, 'services.html')

def web_dev(request):
    return render(request, 'web_dev.html')

def app_dev(request):
    return render(request, 'app_dev.html')

def seo(request):
    return render(request, 'seo.html')

def video_editing(request):
    return render(request, 'video_editing.html')

def cloud_hosting(request):
    return render(request, 'cloud_hosting.html')

def custom_tech(request):
    return render(request, 'custom_tech.html')

def digital_marketing(request):
    return render(request, 'digital_marketing.html')

# --- LEGAL PAGES ---
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

# --- CONTACT & CAREER ---
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company', 'Not Provided')
        service_type = request.POST.get('service_type', 'Not Provided')
        budget = request.POST.get('budget', 'Not Provided')
        message = request.POST.get('message', '')
        
        ContactLead.objects.create(
            name=name, phone=phone, email=email, company=company,
            service_type=service_type, budget=budget, message=message
        )
        
        subject = f"🚀 New Project Lead: {name} | TechPixels"
        email_body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nService Type: {service_type}\nMessage: {message}"
        
        try:
            send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['techpixelsstudio@gmail.com'], fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e) 
        
        # Pop-up & Redirect to Contact
        context = {
            'swal_trigger': True,
            'swal_msg': "Your inquiry has been submitted! Our senior architect will contact you shortly.",
            'redirect_url': '/contact/'
        }
        return render(request, 'contact.html', context)
        
    return render(request, 'contact.html')

def career(request):
    jobs = JobOpening.objects.filter(is_active=True).order_by('-created_at')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        portfolio = request.POST.get('portfolio', 'Not Provided')
        short_note = request.POST.get('short_note', '')
        resume = request.FILES.get('resume') 

        JobApplication.objects.create(
            full_name=full_name, email=email, role=role,
            portfolio=portfolio, short_note=short_note, resume=resume
        )

        subject = f"🎯 New Job Application: {full_name} applied for {role}"
        email_body = f"Name: {full_name}\nEmail: {email}\nRole Applied For: {role}\nPortfolio: {portfolio}\n\nWhy TechPixels?\n{short_note}"

        try:
            msg = EmailMessage(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['techpixelsstudio@gmail.com'])
            if resume:
                msg.attach(resume.name, resume.read(), resume.content_type)
            msg.send(fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e)

        # Pop-up & Redirect to Career
        context = {
            'jobs': jobs,
            'swal_trigger': True,
            'swal_msg': "Message Sent Successfully! We will review your application and get back to you soon.",
            'redirect_url': '/career/'
        }
        return render(request, 'career.html', context)

    return render(request, 'career.html', {'jobs': jobs})

# --- NEWSLETTER AJAX ---
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            return JsonResponse({'status': 'success', 'message': 'Welcome to the club! You will receive our next insights soon.'})
        return JsonResponse({'status': 'error', 'message': 'Please provide a valid email.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)