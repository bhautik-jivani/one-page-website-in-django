from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from ych_admin.models import *

def ych_home(request):
    return redirect('/')

def ych_base(request):
    homeData = Home.objects.all()
    menus = Menu.objects.all()
    homeButtons = HomeButton.objects.all()
    today = timezone.now()
    today = today.strftime("%d %b %Y")

    # Services
    services = Service.objects.all()

    # About-us
    aboutus = About.objects.all()
    context = {
        "homeData": homeData, 
        "menus":menus, 
        "homeButtons": homeButtons,
        "services": services,
        "aboutus": aboutus,
        "today": today,
    }
    
    return render(request, 'base.html', context )

