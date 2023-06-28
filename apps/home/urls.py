from django.urls import path
from apps.home import views

app_name = "home"

urlpatterns = [
	path("", views.index, name="index"),
	path("about", views.about, name="about"),
	path("services", views.services, name="services"),
	path("contact", views.contact, name="contact"),
	path("appointment", views.appointment, name="appointment"),

]