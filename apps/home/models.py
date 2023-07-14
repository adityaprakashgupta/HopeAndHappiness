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
