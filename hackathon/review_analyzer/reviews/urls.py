from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Create this file in 'templates'

from django.urls import path
from .views import analyze_reviews, home

urlpatterns = [
    path('', home, name='home'),  # 👈 This is the missing part
    path('analyze/', analyze_reviews, name='analyze_reviews'),
]
