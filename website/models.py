from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class SiteSettings(models.Model):
    org_name = models.CharField(max_length=200, default='Kids Alive Kenya')
    tagline = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    mission_statement = models.TextField(blank=True)
    vision_statement = models.TextField(blank=True)
    about_story = models.TextField(blank=True, verbose_name='Our Story')
    about_story_image = models.ImageField(upload_to='about/', blank=True, null=True)

    value_1_title = models.CharField(max_length=100, blank=True)
    value_1_text = models.TextField(blank=True)
    value_1_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-heart',
                                     help_text='Font Awesome class e.g. fa-solid fa-heart')
    value_2_title = models.CharField(max_length=100, blank=True)
    value_2_text = models.TextField(blank=True)
    value_2_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-hands-holding-child',
                                     help_text='Font Awesome class e.g. fa-solid fa-hands-holding-child')
    value_3_title = models.CharField(max_length=100, blank=True)
    value_3_text = models.TextField(blank=True)
    value_3_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-seedling',
                                     help_text='Font Awesome class e.g. fa-solid fa-seedling')

    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    map_embed_url = models.URLField(blank=True, help_text='Google Maps embed src URL')
    donate_url = models.URLField(blank=True, help_text='External donation link')
    volunteer_info = models.TextField(blank=True)

    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    footer_tagline = models.CharField(max_length=300, blank=True)
    copyright_text = models.CharField(max_length=200, blank=True,
                                       default='© Kids Alive Kenya. All rights reserved.')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.org_name

    def save(self, *args, **kwargs):
        # Enforce singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class NavItem(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_external = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Navigation Item'

    def __str__(self):
        return self.label


class HeroSection(models.Model):
    headline = models.CharField(max_length=300)
    subheadline = models.TextField(blank=True)
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    background_video_url = models.URLField(blank=True)
    primary_cta_text = models.CharField(max_length=100, default='Learn More')
    primary_cta_url = models.CharField(max_length=200, default='/about/')
    secondary_cta_text = models.CharField(max_length=100, blank=True, default='Donate Now')
    secondary_cta_url = models.CharField(max_length=200, blank=True, default='/get-involved/')
    is_active = models.BooleanField(default=True)
    overlay_opacity = models.DecimalField(max_digits=3, decimal_places=2, default='0.55',
                                           help_text='0.0 (transparent) to 1.0 (opaque)')

    class Meta:
        verbose_name = 'Hero Section'

    def __str__(self):
        return self.headline[:80]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={
            'headline': 'Transforming Lives in Kenya',
            'subheadline': 'Giving vulnerable children hope, education, and a future.',
        })
        return obj


class Program(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    tagline = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='fa-solid fa-circle',
                             help_text='Font Awesome class e.g. fa-solid fa-graduation-cap')
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    cta_text = models.CharField(max_length=100, blank=True, default='Learn More')
    cta_url = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ImpactStat(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=50, help_text='e.g. 500, 10+, 3')
    suffix = models.CharField(max_length=20, blank=True, help_text='e.g. +, %, K')
    icon = models.CharField(max_length=100, default='fa-solid fa-chart-line',
                             help_text='Font Awesome class e.g. fa-solid fa-children')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Impact Statistic'

    def __str__(self):
        return f'{self.value}{self.suffix} {self.label}'


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'

    def __str__(self):
        return f'{self.name} – {self.role}'


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, help_text='e.g. Parent, Volunteer, Alumni')
    quote = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name}: "{self.quote[:60]}..."'


class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True, max_length=400,
                                help_text='Short summary shown in listing pages (max 400 chars)')
    body = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'News Post'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('health', 'Health'),
        ('community', 'Community'),
        ('events', 'Events'),
        ('general', 'General'),
    ]
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Gallery Image'

    def __str__(self):
        return self.caption or f'Gallery image #{self.pk}'


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    url = models.URLField(blank=True)
    is_donor = models.BooleanField(default=False, help_text='Check if this is a donor rather than a partner')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-received_at']
        verbose_name = 'Contact Message'

    def __str__(self):
        return f'{self.name} ({self.email}) – {self.received_at.strftime("%d %b %Y")}'


class Page(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    meta_description = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
