from django.shortcuts import HttpResponse

# Create your views here.

def homepageview(request):
    return HttpResponse('Hello, World!')