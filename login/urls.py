# Assuming your views.py contains a function named login

from django.urls import path
from .views import login

urlpatterns = [
    path('', login, name='login'),
    # other URL patterns...
]
