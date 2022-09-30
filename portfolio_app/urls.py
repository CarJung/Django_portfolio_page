from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name ='portfolio_app'

urlpatterns = [
    path('KW/', views.main_view),
    path('KW/CV/', views.cv_view),
    path('KW/Diabetes/', views.Diabetes_view),
    path('KW/Seizure/', views.Seizure_view),
    path('KW/Stat_app/', views.Stat_app_view),
    path('KW/Estates/', views.Estates_view),
    path('KW/Data_camp/', views.data_camp_view),
]