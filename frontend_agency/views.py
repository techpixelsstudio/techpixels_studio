from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import JsonResponse # <--- Yellow line fix (Import added)
from .models import ContactLead, JobApplication, JobOpening, BlogPost, InstagramReel

# --- MAIN PAGES ---
def home(request):
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
            send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['mohannikam988@gmail.com'], fail_silently=False)
        except Exception as e:
            print("Email sending failed:", e)
            
        messages.success(request, "Tumacha msg amhala milala. Amhi lavkarch tumchyashi contact karu!")
        return redirect('home')
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

# --- BLOG LOGIC (With AUTO-FIX for Empty Slugs) ---
def blog(request):
    # 🔥 AUTO-FIX: Jar kuthlya junya post madhe slug nsel, tar he code automatic slug banvel
    posts_without_slugs = BlogPost.objects.filter(slug='')
    for p in posts_without_slugs:
        p.save() # He automatic slug generate karel

    # Fakt latest 6 posts gheto
    posts = BlogPost.objects.all().order_by('-date_posted')[:6]
    
    # Fakt latest 3 active reels gheto
    reels = InstagramReel.objects.filter(is_active=True).order_by('-created_at')[:3]
    
    return render(request, 'blog.html', {'posts': posts, 'reels': reels})

def all_blogs(request):
    # 🔥 AUTO-FIX here too
    posts_without_slugs = BlogPost.objects.filter(slug='')
    for p in posts_without_slugs:
        p.save()

    # Sagle posts gheto (View All Articles sathi)
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'all_blogs.html', {'posts': posts})

def blog_detail(request, slug):
    # Article vachnyasathi detail page
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
            print("Email failed:", e) 
            
        messages.success(request, "Your inquiry has been submitted! Our senior architect will contact you shortly.")
        return redirect('blog')
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
            msg = EmailMessage(subject, email_body, settings.DEFAULT_FROM_EMAIL, ['mohannikam988@gmail.com'])
            if resume:
                msg.attach(resume.name, resume.read(), resume.content_type)
            msg.send(fail_silently=False)
        except Exception as e:
            print("Email failed:", e)

        messages.success(request, "Tumcha application submit jhala ahe! Aamhi lavkarach tumhala sampark karu.")
        return redirect('career')

    return render(request, 'career.html', {'jobs': jobs})

# --- NEWSLETTER ---
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Pop-up message set karto
            messages.success(request, 'Welcome to the Inner Circle! You will receive our next insights soon.')
            # Aani direct Home page la pathavto
            return redirect('home')
    return redirect('blog')