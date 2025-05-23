from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("career/", views.career, name="career"), 
    path("privacy", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("cookies/", views.cookies, name="cookies")
]
