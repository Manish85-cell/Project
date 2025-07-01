from . import views
from django.urls import path

app_name = "about"
urlpatterns = [
    path('', views.index, name="index"),
     path('intro', views.intro, name="intro"),
    path("blog", views.blog, name="blog"),
    path("cv", views.cv, name="cv"),
    path("contact", views.contact, name="contact")

]