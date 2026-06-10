from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, NavItem, HeroSection, HeroSlide, Program, ImpactStat,
    TeamMember, Testimonial, NewsPost, GalleryImage, Partner,
    ContactMessage, Page,
    Theme, CoreValue, Accreditation, InterventionLevel, Location,
    Activity, TeamRole, ImpactStory,
)

admin.site.site_header = 'Kids Alive Kenya — Site Admin'
admin.site.site_title = 'KAI-K Admin'
admin.site.index_title = 'Content Management'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organisation', {
            'fields': ('org_name', 'tagline', 'logo', 'favicon', 'mission_statement', 'vision_statement'),
        }),
        ('Our Story (About page body)', {
            'fields': ('about_story', 'about_story_image'),
        }),
        ('Contact & Donate', {
            'fields': ('phone', 'email', 'address', 'map_embed_url', 'donate_url', 'volunteer_info'),
        }),
        ('Social Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'youtube_url', 'linkedin_url'),
            'classes': ('collapse',),
        }),
        ('Footer', {
            'fields': ('footer_tagline', 'copyright_text'),
        }),

        # ---- Page content ----
        ('Home Page', {
            'fields': (
                'home_strip_tagline', 'home_strip_heading', 'home_strip_body',
                'home_feature_heading', 'home_feature_body',
                'home_about_heading', 'home_about_body',
                'home_cta_heading', 'home_cta_body',
            ),
            'classes': ('collapse',),
        }),
        ('About Page — Hero & At a Glance', {
            'fields': (
                'about_hero_title', 'about_hero_subtitle', 'about_hero_image',
                'about_glance_type', 'about_glance_country', 'about_glance_headquarters',
                'about_glance_areas', 'about_glance_global_parent', 'about_glance_global_presence',
                'about_glance_children_reached', 'about_glance_scripture',
            ),
            'classes': ('collapse',),
        }),
        ('About Page — Themes, Mission & Vision', {
            'fields': (
                'about_themes_heading', 'about_themes_subtitle',
                'about_mission_heading', 'about_scripture_text', 'about_scripture_ref',
                'vision_1', 'vision_2', 'vision_3', 'vision_4',
            ),
            'classes': ('collapse',),
        }),
        ('About Page — Values & Global Family', {
            'fields': (
                'about_values_subtitle',
                'about_global_heading', 'about_global_body_1', 'about_global_body_2',
            ),
            'classes': ('collapse',),
        }),
        ('Programs Page', {
            'fields': (
                'programs_hero_title', 'programs_hero_subtitle', 'programs_hero_image',
                'programs_levels_subtitle', 'programs_locations_subtitle',
                'programs_activities_intro',
                'mdt_intro', 'safeguarding_text',
                'programs_cta_heading', 'programs_cta_body',
            ),
            'classes': ('collapse',),
        }),
        ('Get Involved / Contact Page', {
            'fields': (
                'get_involved_hero_title', 'get_involved_hero_subtitle', 'get_involved_hero_image',
                'volunteer_heading',
                'partner_heading', 'partner_body',
                'schools_heading', 'schools_body',
            ),
            'classes': ('collapse',),
        }),
        ('Impact Page', {
            'fields': (
                'impact_hero_title', 'impact_hero_subtitle', 'impact_hero_image',
                'impact_stories_subtitle',
                'impact_cta_heading', 'impact_cta_body',
            ),
            'classes': ('collapse',),
        }),
        ('Gallery Page', {
            'fields': (
                'gallery_hero_title', 'gallery_hero_subtitle', 'gallery_hero_image',
                'gallery_cta_heading', 'gallery_cta_body',
            ),
            'classes': ('collapse',),
        }),
        ('Contact Page', {
            'fields': ('contact_hero_title', 'contact_hero_subtitle', 'contact_hero_image'),
            'classes': ('collapse',),
        }),
        ('News Page', {
            'fields': (
                'news_hero_title', 'news_hero_subtitle', 'news_hero_image',
                'news_sidebar_cta_heading', 'news_sidebar_cta_body',
            ),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'order', 'is_external', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Content', {'fields': ('headline', 'subheadline')}),
        ('Background', {'fields': ('background_image', 'background_video_url', 'overlay_opacity')}),
        ('Calls to Action', {'fields': ('primary_cta_text', 'primary_cta_url', 'secondary_cta_text', 'secondary_cta_url')}),
        ('Status', {'fields': ('is_active',)}),
    )

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'image_preview')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
    fieldsets = (
        ('Content', {'fields': ('title', 'subtitle', 'button_text')}),
        ('Image', {'fields': ('image',)}),
        ('Settings', {'fields': ('order', 'is_active')}),
    )

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:4px;object-fit:cover;">',
                obj.image.url,
            )
        return '—'


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(InterventionLevel)
class InterventionLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'icon_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'badge', 'focus', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('text', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(ImpactStory)
class ImpactStoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'person_name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    ordering = ('order',)

    @admin.display(description='Icon Preview')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'suffix', 'icon_preview', 'order')
    list_editable = ('order',)
    ordering = ('order',)

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        return format_html('<i class="{}"></i> <code>{}</code>', obj.icon, obj.icon)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role')
    ordering = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    ordering = ('order',)


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published', 'is_featured')
    list_editable = ('is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'published_date')
    search_fields = ('title', 'body', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'category', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    ordering = ('order',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_donor', 'url', 'order')
    list_editable = ('order', 'is_donor')
    ordering = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'received_at', 'is_read')
    list_filter = ('is_read', 'received_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'received_at')
    ordering = ('-received_at',)

    def has_add_permission(self, request):
        return False


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
