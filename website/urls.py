from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('impact/', views.impact, name='impact'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('contact/', views.contact, name='contact'),
]
