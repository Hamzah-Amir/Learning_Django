from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutViewPage.as_view(), name="about"),
    path('', HomePageView.as_view(), name='home'),
    
]