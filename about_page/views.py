from django.shortcuts import render
from .models import About

def about_view(request):
    about_content = About.objects.first()
    return render(request, 'about_page/about.html', {'about': about_content})