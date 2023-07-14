from django.shortcuts import render

def about(request):
	return render(request, "home/about-me.html")

def services(request):
	return render(request, "home/services.html")

def contact(request):
	return render(request, "home/contact.html")

def appointment(request):
	return render(request, "home/appointment.html")
