from django.shortcuts import render
from .models import HeroSection

# Create your views here.
def index(request):
	context = {
		"HeroSectionData": HeroSection.objects.all().order_by("updated_at")
	}
	return render(request, "home/index.html", context)

def about(request):
	return render(request, "home/about-me.html")

def services(request):
	return render(request, "home/services.html")

def contact(request):
	return render(request, "home/contact.html")