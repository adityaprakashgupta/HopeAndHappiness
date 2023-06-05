from django.contrib import admin
from .models import HeroSection
from .forms import HeroSectionForm

# Register your models here.
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
	form = HeroSectionForm
	list_display = ('heading','image')