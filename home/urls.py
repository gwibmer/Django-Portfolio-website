from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Gerardo Wibmer Portfolio"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to the Admin Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('#contact', views.contact, name='contact'),
]
