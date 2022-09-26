from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name ='portfolio_app'

urlpatterns = [
    path('KW_portfolio', views.main_view),

]