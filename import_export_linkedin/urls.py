# import_export_linkedin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('scrape-linkedin-profile/', views.scrape_linkedin_profile, name='scrape_linkedin_profile'),
]