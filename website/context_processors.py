from .models import SiteSettings, NavItem


def site_globals(request):
    return {
        'site': SiteSettings.get(),
        'nav_items': NavItem.objects.filter(is_active=True).order_by('order'),
    }
