from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    # path('login', views.index),
    path('contests', views.index),
    path('problems', views.index),
    path('signup', views.index),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('editor', views.editor,name="editor"),
    path('editor2', views.index),
    path('submit', views.submit, name = "submit")
]