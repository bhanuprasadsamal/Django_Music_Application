from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('playlist/', views.playlist, name='playlist'),
    path('contact/', views.contact, name='contact'),
]

