from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name ='portfolio_app'

urlpatterns = [
    path('KW/', views.main_view),
    path('Template/', views.template_view),
    path('Project/', views.project_view),
]