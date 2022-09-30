from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name ='portfolio_app'

urlpatterns = [
    path('KW/', views.main_view),
    path('CV/', views.cv_view),
    path('Diabetes/', views.Diabetes_view),
    path('Seizure/', views.Seizure_view),
    path('Stat_app/', views.Stat_app_view),
    path('Estates/', views.Estates_view),
    path('Data_camp/', views.data_camp_view),
]