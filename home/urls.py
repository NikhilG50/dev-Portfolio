from django.urls import path
from django.contrib import admin
from . import views


admin.site.site_header = "Login to Portfolio management"
admin.site.site_title = "Welcome to Nikhil's dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='contact'),
]
