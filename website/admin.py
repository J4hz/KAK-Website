from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, NavItem, HeroSection, Program, ImpactStat,
    TeamMember, Testimonial, NewsPost, GalleryImage, Partner,
    ContactMessage, Page,
)

admin.site.site_header = 'Kids Alive Kenya — Site Admin'
admin.site.site_title = 'KAI-K Admin'
admin.site.index_title = 'Content Management'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organisation', {'fields': ('org_name', 'tagline', 'logo', 'favicon')}),
        ('Mission & Vision', {'fields': ('mission_statement', 'vision_statement')}),
        ('About / Our Story', {'fields': ('about_story', 'about_story_image')}),
        ('Brand Values', {'fields': (
            'value_1_icon', 'value_1_title', 'value_1_text',
            'value_2_icon', 'value_2_title', 'value_2_text',
            'value_3_icon', 'value_3_title', 'value_3_text',
        )}),
        ('Contact', {'fields': ('phone', 'email', 'address', 'map_embed_url')}),
        ('Donate & Volunteer', {'fields': ('donate_url', 'volunteer_info')}),
        ('Social Links', {'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'youtube_url', 'linkedin_url')}),
        ('Footer', {'fields': ('footer_tagline', 'copyright_text')}),
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
