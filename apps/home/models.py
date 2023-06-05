from django.db import models
from nanoid import generate

# Create your models here.
def make_nanoid():
	return generate(size=16)


class UtilModel(models.Model):
	id = models.CharField(max_length=16, default=make_nanoid, primary_key=True, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
	
class HeroSection(UtilModel):
	heading = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='home/image/HeroSection', help_text="Image should be of dimention 1045x720.")