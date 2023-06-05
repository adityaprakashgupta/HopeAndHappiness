from django.core.files.images import get_image_dimensions
from django import forms
from .models import HeroSection

class HeroSectionForm(forms.ModelForm):
	class Meta:
		model = HeroSection
		fields = '__all__'

	def clean_image(self):
		image = self.cleaned_data.get("image")
		if not image:
			raise forms.ValidationError("Image field is required.")
		else:
			w, h = get_image_dimensions(image)
			if w != 1045 and h != 720:
				raise forms.ValidationError("Image should be of dimention 1045x720.")
		return image


