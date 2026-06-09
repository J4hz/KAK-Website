from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import (
    HeroSection, Program, ImpactStat, TeamMember, Testimonial,
    NewsPost, GalleryImage, Partner, ContactMessage, SiteSettings,
    Theme, CoreValue, Accreditation, InterventionLevel, Location,
    Activity, TeamRole, ImpactStory,
)
from .forms import ContactForm


def home(request):
    hero = HeroSection.get()

    hero_slides_qs = HeroSection.objects.filter(is_active=True).order_by('pk')
    hero_slides = []
    for slide in hero_slides_qs:
        hero_slides.append({
            'title': slide.headline,
            'subtitle': slide.subheadline,
            'image_url': slide.background_image.url if slide.background_image else None,
            'button_primary': slide.primary_cta_text,
            'button_secondary': slide.secondary_cta_text,
        })

    featured_programs = Program.objects.filter(is_featured=True).order_by('order')[:3]
    features = None
    if featured_programs.exists():
        features = {
            'label': 'Features',
            'title': 'What we do matters',
            'subtitle': 'These pillars lead our work in Kenya',
            'items': [
                {'icon': p.icon, 'title': p.name, 'description': p.tagline or p.description[:120]}
                for p in featured_programs
            ],
        }

    stats = ImpactStat.objects.all().order_by('order')[:4]
    testimonials = Testimonial.objects.filter(is_featured=True).order_by('order')[:3]
    children_stat = ImpactStat.objects.order_by('order').first()

    return render(request, 'website/home.html', {
        'hero': hero,
        'hero_slides': hero_slides,
        'features': features,
        'stats': stats,
        'testimonials': testimonials,
        'children_stat': children_stat,
    })


def about(request):
    team = TeamMember.objects.filter(is_active=True).order_by('order')
    photos = GalleryImage.objects.all().order_by('order')[:8]
    themes = Theme.objects.filter(is_active=True).order_by('order')
    values = CoreValue.objects.filter(is_active=True).order_by('order')
    accreditations = Accreditation.objects.filter(is_active=True).order_by('order')
    return render(request, 'website/about.html', {
        'team': team,
        'photos': photos,
        'themes': themes,
        'values': values,
        'accreditations': accreditations,
    })


def programs(request):
    all_programs = Program.objects.all().order_by('order')
    photos = GalleryImage.objects.all().order_by('order')[8:14]
    levels = InterventionLevel.objects.filter(is_active=True).order_by('order')
    locations = Location.objects.filter(is_active=True).order_by('order')
    activities = Activity.objects.filter(is_active=True).order_by('order')
    team_roles = TeamRole.objects.filter(is_active=True).order_by('order')
    return render(request, 'website/programs.html', {
        'programs': all_programs,
        'photos': photos,
        'levels': levels,
        'locations': locations,
        'activities': activities,
        'team_roles': team_roles,
    })


def impact(request):
    stats = ImpactStat.objects.all().order_by('order')
    testimonials = Testimonial.objects.filter(is_featured=True).order_by('order')
    stories = NewsPost.objects.filter(is_published=True, is_featured=True)[:4]
    gallery = GalleryImage.objects.all().order_by('order')
    impact_stories = ImpactStory.objects.filter(is_active=True).order_by('order')
    return render(request, 'website/impact.html', {
        'stats': stats,
        'testimonials': testimonials,
        'stories': stories,
        'gallery': gallery,
        'impact_stories': impact_stories,
    })


def news_list(request):
    posts_qs = NewsPost.objects.filter(is_published=True).order_by('-published_date')
    paginator = Paginator(posts_qs, 9)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'website/news_list.html', {'page_obj': page_obj})


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    related = NewsPost.objects.filter(is_published=True).exclude(pk=post.pk).order_by('-published_date')[:3]
    return render(request, 'website/news_detail.html', {'post': post, 'related': related})


def gallery(request):
    category = request.GET.get('category', 'all')
    images = GalleryImage.objects.all().order_by('order', 'pk')
    categories = (
        GalleryImage.objects
        .values_list('category', flat=True)
        .distinct()
        .order_by('category')
    )
    if category != 'all':
        images = images.filter(category=category)
    return render(request, 'website/gallery.html', {
        'images': images,
        'categories': categories,
        'active_category': category,
    })


def get_involved(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.subject = 'Volunteer Inquiry'
            msg.save()
            messages.success(request, 'Thank you for your interest! We will be in touch soon.')
            return redirect('get_involved')
    else:
        form = ContactForm()
    locations = Location.objects.filter(is_active=True).order_by('order')
    return render(request, 'website/get_involved.html', {
        'form': form,
        'locations': locations,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been received. We will respond within 2 business days.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
