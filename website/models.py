from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class SiteSettings(models.Model):
    # --- Identity ---
    org_name = models.CharField(max_length=200, default='Kids Alive Kenya')
    tagline = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    mission_statement = models.TextField(blank=True)
    vision_statement = models.TextField(blank=True)
    about_story = models.TextField(blank=True, verbose_name='Our Story')
    about_story_image = models.ImageField(upload_to='about/', blank=True, null=True)

    # --- Legacy value fields (kept for data safety) ---
    value_1_title = models.CharField(max_length=100, blank=True)
    value_1_text = models.TextField(blank=True)
    value_1_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-heart')
    value_2_title = models.CharField(max_length=100, blank=True)
    value_2_text = models.TextField(blank=True)
    value_2_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-hands-holding-child')
    value_3_title = models.CharField(max_length=100, blank=True)
    value_3_text = models.TextField(blank=True)
    value_3_icon = models.CharField(max_length=100, blank=True, default='fa-solid fa-seedling')

    # --- Contact ---
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    map_embed_url = models.URLField(blank=True, help_text='Google Maps embed src URL')
    donate_url = models.URLField(blank=True, help_text='External donation link')
    volunteer_info = models.TextField(blank=True)

    # --- Social ---
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    # --- Footer ---
    footer_tagline = models.CharField(max_length=300, blank=True)
    copyright_text = models.CharField(max_length=200, blank=True,
                                       default='© Kids Alive Kenya. All rights reserved.')

    # =========================================================
    # HOME PAGE
    # =========================================================
    home_strip_tagline = models.CharField(
        max_length=300, blank=True,
        default='Trauma into Triumph | Justice that Heals | Bonds that Mend',
        verbose_name='Strip tagline')
    home_strip_heading = models.CharField(
        max_length=300, blank=True,
        default='Restorative education, family strengthening, protective care, justice advocacy',
        verbose_name='Strip heading')
    home_strip_body = models.TextField(
        blank=True,
        default='KAI-K runs five complementary programs across Nairobi, Nyeri, and Kisii counties — meeting children where they are and walking with them toward healing and wholeness.',
        verbose_name='Strip body text')
    home_feature_heading = models.CharField(
        max_length=200, blank=True,
        default='We do the hard things',
        verbose_name='Feature box heading')
    home_feature_body = models.TextField(
        blank=True,
        default='We go where others won’t, and we do what others don’t — hard stories, complex trauma, legal processes, and deep systemic brokenness. Places where others often cannot go.',
        verbose_name='Feature box body text')
    home_about_heading = models.CharField(
        max_length=300, blank=True,
        default='We believe every child deserves a future',
        verbose_name='About section heading')
    home_about_body = models.TextField(
        blank=True,
        default='Kids Alive Kenya is committed to rescuing, restoring, and raising children who will transform their world. We walk with children and families through the hardest realities — because every child is cherished by God.',
        verbose_name='About section body text')
    home_cta_heading = models.CharField(
        max_length=200, blank=True,
        default='Start making a difference',
        verbose_name='CTA heading')
    home_cta_body = models.CharField(
        max_length=400, blank=True,
        default='Every contribution transforms a child’s life. Choose your way to help today.',
        verbose_name='CTA body text')

    # =========================================================
    # ABOUT PAGE
    # =========================================================
    about_hero_title = models.CharField(
        max_length=300, blank=True,
        default='We go where others won’t. We do what others don’t.',
        verbose_name='Hero title')
    about_hero_subtitle = models.TextField(
        blank=True,
        default='Kids Alive International Kenya has served vulnerable children and families across Kenya for over 20 years — rooted in faith, driven by justice.',
        verbose_name='Hero subtitle')
    about_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    about_glance_type = models.CharField(
        max_length=200, blank=True, default='Non-profit faith-based NGO',
        verbose_name='At a Glance — Type')
    about_glance_country = models.CharField(
        max_length=100, blank=True, default='Kenya',
        verbose_name='At a Glance — Country')
    about_glance_headquarters = models.CharField(
        max_length=200, blank=True, default='Nairobi, Kenya',
        verbose_name='At a Glance — Headquarters')
    about_glance_areas = models.CharField(
        max_length=300, blank=True, default='Nairobi | Nyeri | Kisii Counties',
        verbose_name='At a Glance — Areas of operation')
    about_glance_global_parent = models.CharField(
        max_length=300, blank=True, default='Kids Alive International (founded 1916, USA)',
        verbose_name='At a Glance — Global parent')
    about_glance_global_presence = models.CharField(
        max_length=300, blank=True,
        default='Active in 8+ countries across Africa, Latin America, Asia and the Middle East',
        verbose_name='At a Glance — Global presence')
    about_glance_children_reached = models.CharField(
        max_length=100, blank=True, default='Over 800 children through KAI-K programs',
        verbose_name='At a Glance — Children reached')
    about_glance_scripture = models.CharField(
        max_length=100, blank=True, default='Isaiah 1:17',
        verbose_name='At a Glance — Scripture reference')
    about_themes_heading = models.CharField(
        max_length=300, blank=True,
        default='Trauma into Triumph. Justice that Heals. Bonds that Mend.',
        verbose_name='Themes section heading')
    about_themes_subtitle = models.CharField(
        max_length=400, blank=True,
        default='Three interlocking convictions that shape everything we do for children and families.',
        verbose_name='Themes section subtitle')
    about_mission_heading = models.CharField(
        max_length=200, blank=True,
        default='Learn to do good. Seek justice.',
        verbose_name='Mission section heading')
    about_scripture_text = models.TextField(
        blank=True,
        default='Learn to do good. Seek justice. Rebuke the oppressor. Defend the fatherless. Plead for the widow.',
        verbose_name='Scripture quote text')
    about_scripture_ref = models.CharField(
        max_length=100, blank=True, default='Isaiah 1:17',
        verbose_name='Scripture reference')
    about_values_subtitle = models.TextField(
        blank=True,
        default='We believe we are God’s children: clean, powerful, a masterpiece, and chosen for a purpose. Every child, parent, and team member we work with is precious to Jesus — worthy of love, justice, and healing.',
        verbose_name='Values section subtitle')
    vision_1 = models.CharField(
        max_length=300, blank=True,
        default='Enjoy a vibrant, life-changing relationship with God.',
        verbose_name='Vision point 1')
    vision_2 = models.CharField(
        max_length=300, blank=True,
        default='Experience emotional and physical well-being.',
        verbose_name='Vision point 2')
    vision_3 = models.CharField(
        max_length=300, blank=True,
        default='Be equipped for a life of independence and service.',
        verbose_name='Vision point 3')
    vision_4 = models.CharField(
        max_length=300, blank=True,
        default='Live life in family and community, free of fear and violence.',
        verbose_name='Vision point 4')
    about_global_heading = models.CharField(
        max_length=200, blank=True, default='Part of something bigger',
        verbose_name='Global family heading')
    about_global_body_1 = models.TextField(
        blank=True,
        default='Kids Alive International Kenya is part of Kids Alive International, a Christian non-profit founded in 1916 by missionaries Leslie and Ava Anglin. What began in Shantung Province, China, has grown into work spanning countries in Central America, South America, Africa, the Middle East, and Asia.',
        verbose_name='Global family paragraph 1')
    about_global_body_2 = models.TextField(
        blank=True,
        default='Being part of this global family means access to proven models, shared research, and a network of people committed to the same mission — the flourishing of vulnerable children everywhere.',
        verbose_name='Global family paragraph 2')

    # =========================================================
    # PROGRAMS PAGE
    # =========================================================
    programs_hero_title = models.CharField(
        max_length=300, blank=True, default='Our programs',
        verbose_name='Hero title')
    programs_hero_subtitle = models.TextField(
        blank=True,
        default='Restorative education, family strengthening, protective care, justice advocacy, and community health — working across Nairobi, Nyeri, and Kisii counties.',
        verbose_name='Hero subtitle')
    programs_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    programs_levels_subtitle = models.TextField(
        blank=True,
        default='KAI-K operates across five complementary areas, designed to meet children where they are and walk with them toward healing and wholeness.',
        verbose_name='Intervention levels subtitle')
    programs_locations_subtitle = models.TextField(
        blank=True,
        default='Our programs run in three counties, covering both rural and urban communities. Each Hope Centre connects families with social services, legal support, livelihoods training, and spiritual care.',
        verbose_name='Locations section subtitle')
    programs_activities_intro = models.TextField(
        blank=True,
        default='Across all our locations, we carry out the following activities to bring healing, justice, and hope to children and families:',
        verbose_name='Activities intro text')
    mdt_intro = models.TextField(
        blank=True,
        default='KAI-K employs social workers, teachers, psychologists, lawyers, and spiritual leads. These staff work together to make sure each child receives care across legal, psychological, educational, and spiritual areas.',
        verbose_name='Multi-disciplinary team intro')
    safeguarding_text = models.TextField(
        blank=True,
        default='We are committed to safe spaces, strong boundaries, and robust protection policies for every child in our care.',
        verbose_name='Safeguarding statement')
    programs_cta_heading = models.CharField(
        max_length=200, blank=True, default='Partner with us',
        verbose_name='CTA heading')
    programs_cta_body = models.CharField(
        max_length=300, blank=True,
        default='Your support — financial, professional, or in prayer — makes this work possible.',
        verbose_name='CTA body text')

    # =========================================================
    # GET INVOLVED / CONTACT PAGE
    # =========================================================
    get_involved_hero_title = models.CharField(
        max_length=300, blank=True, default='Get in touch',
        verbose_name='Hero title')
    get_involved_hero_subtitle = models.TextField(
        blank=True,
        default='We would love to hear from you. Find us at our centres across Nairobi, Nyeri, and Kisii counties.',
        verbose_name='Hero subtitle')
    get_involved_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    volunteer_heading = models.CharField(
        max_length=200, blank=True, default='Volunteer',
        verbose_name='Volunteer section heading')
    partner_heading = models.CharField(
        max_length=200, blank=True, default='Partner with us',
        verbose_name='Partner section heading')
    partner_body = models.TextField(
        blank=True,
        default='Is your organisation looking to partner with a credible, faith-based NGO with deep roots in the Kenyan community? We are open to institutional partnerships, church collaborations, and corporate CSR programmes.',
        verbose_name='Partner section body text')
    schools_heading = models.CharField(
        max_length=200, blank=True, default='Schools and institutions',
        verbose_name='Schools section heading')
    schools_body = models.TextField(
        blank=True,
        default='KAI-K partners with public and private schools, county governments, and child-serving institutions to provide trauma-informed care training for staff who work with children. If your school or institution would like to equip your team with the knowledge and skills to care for children in a trauma-informed way, we would be glad to hear from you.',
        verbose_name='Schools section body text')

    # =========================================================
    # IMPACT PAGE
    # =========================================================
    impact_hero_title = models.CharField(
        max_length=300, blank=True, default='Our impact',
        verbose_name='Hero title')
    impact_hero_subtitle = models.TextField(
        blank=True,
        default='Real numbers. Real lives. Real transformation in Kenya.',
        verbose_name='Hero subtitle')
    impact_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    impact_stories_subtitle = models.CharField(
        max_length=300, blank=True,
        default='These are real lives touched by KAI-K — names changed to protect privacy.',
        verbose_name='Stories section subtitle')
    impact_cta_heading = models.CharField(
        max_length=200, blank=True, default='Be part of this story',
        verbose_name='CTA heading')
    impact_cta_body = models.CharField(
        max_length=300, blank=True,
        default='Your support writes the next chapter for a child in Kenya.',
        verbose_name='CTA body text')

    # =========================================================
    # GALLERY PAGE
    # =========================================================
    gallery_hero_title = models.CharField(
        max_length=300, blank=True, default='Gallery',
        verbose_name='Hero title')
    gallery_hero_subtitle = models.TextField(
        blank=True,
        default='Moments of learning, joy, and transformation from across our programs in Kenya.',
        verbose_name='Hero subtitle')
    gallery_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    gallery_cta_heading = models.CharField(
        max_length=200, blank=True, default='Help us write more stories like these',
        verbose_name='CTA heading')
    gallery_cta_body = models.CharField(
        max_length=300, blank=True,
        default='Every photo tells a story made possible by supporters like you.',
        verbose_name='CTA body text')

    # =========================================================
    # CONTACT PAGE
    # =========================================================
    contact_hero_title = models.CharField(
        max_length=300, blank=True, default='Contact us',
        verbose_name='Hero title')
    contact_hero_subtitle = models.TextField(
        blank=True,
        default='We would love to hear from you. Reach out and we will respond within 2 business days.',
        verbose_name='Hero subtitle')
    contact_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')

    # =========================================================
    # NEWS PAGE
    # =========================================================
    news_hero_title = models.CharField(
        max_length=300, blank=True, default='News & stories',
        verbose_name='Hero title')
    news_hero_subtitle = models.TextField(
        blank=True,
        default='Stories of hope and transformation from across Kenya.',
        verbose_name='Hero subtitle')
    news_hero_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Hero background image',
        help_text='Leave blank to use the default static image')
    news_sidebar_cta_heading = models.CharField(
        max_length=200, blank=True, default='Support our work',
        verbose_name='Sidebar CTA heading')
    news_sidebar_cta_body = models.TextField(
        blank=True,
        default='Your generosity directly funds programs like the ones described in this story.',
        verbose_name='Sidebar CTA body text')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.org_name

    def save(self, *args, **kwargs):
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


class HeroSlide(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    button_text = models.CharField(
        max_length=100, blank=True, default='Learn more',
        help_text='Text for the slide button (links to About page)')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Home Page Slide'
        verbose_name_plural = 'Home Page Slides'

    def __str__(self):
        return self.title


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


# =============================================================================
# NEW CONTENT MODELS
# =============================================================================

class Theme(models.Model):
    icon = models.CharField(max_length=100, default='fa-solid fa-circle',
                             help_text='Font Awesome class e.g. fa-solid fa-trophy')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    icon = models.CharField(max_length=100, default='fa-solid fa-circle',
                             help_text='Font Awesome class e.g. fa-solid fa-cross')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Core Value'

    def __str__(self):
        return self.title


class Accreditation(models.Model):
    icon = models.CharField(max_length=100, default='fa-solid fa-star',
                             help_text='Font Awesome class e.g. fa-solid fa-star')
    icon_color = models.CharField(max_length=50, blank=True, default='#f59e0b',
                                   help_text='CSS colour value e.g. #f59e0b or var(--color-primary)')
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class InterventionLevel(models.Model):
    icon = models.CharField(max_length=100, default='fa-solid fa-circle',
                             help_text='Font Awesome class e.g. fa-solid fa-graduation-cap')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True,
                                 help_text='e.g. Nyeri County or All locations')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Intervention Level'

    def __str__(self):
        return self.title


class Location(models.Model):
    badge = models.CharField(max_length=100, help_text='County name e.g. Nyeri County')
    name = models.CharField(max_length=200, help_text='Centre or facility name')
    focus = models.CharField(max_length=300, help_text='Program focus description')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Activity(models.Model):
    text = models.CharField(max_length=300)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.text[:80]


class TeamRole(models.Model):
    icon = models.CharField(max_length=100, default='fa-solid fa-circle',
                             help_text='Font Awesome class e.g. fa-solid fa-gavel')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Team Role'

    def __str__(self):
        return self.title


class ImpactStory(models.Model):
    label = models.CharField(max_length=200, help_text='Story label e.g. Linnet’s Story')
    body = models.TextField()
    person_name = models.CharField(max_length=200, blank=True,
                                    help_text='Name shown below the story (can be pseudonym)')
    name_note = models.CharField(max_length=200, blank=True,
                                  default='Name changed to protect privacy')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Impact Story'
        verbose_name_plural = 'Impact Stories'

    def __str__(self):
        return self.label
