from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('about/', AboutViewPage.as_view(), name="About Page")
    
]