from django.db import models
from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField
from filer.fields.image import FilerImageField


class HTMLTagPluginModel(CMSPlugin):
    TAG_CHOICES = [
        ("h1", "Heading 1"),
        ("h2", "Heading 2"),
        ("h3", "Heading 3"),
        ("h4", "Heading 4"),
        ("h5", "Heading 5"),
        ("h7", "Heading 6"),
        ("p", "Paragraph"),
        ("span", "Span"),
        ("div", "Div"),
        # Add more tag choices as needed
    ]

    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    content = models.TextField()
    attributes = AttributesField()


class HeroChildPlugin(CMSPlugin):
    heading = models.CharField(max_length=50)
    description = models.TextField()
    image = FilerImageField(verbose_name='Image', blank=False, null=True, on_delete=models.SET_NULL, related_name='+', help_text="Image should be of dimention 1045x720."
    )

    def __str__(self):
        return ' '

class FeatureModel(CMSPlugin):
    h31 = models.CharField(verbose_name="Heading Text 1", max_length=50)
    p1 = models.TextField(verbose_name="Paragraph Text 1")
    h32 = models.CharField(verbose_name="Heading Text 2", max_length=50)
    p2 = models.TextField(verbose_name="Paragraph Text 2")
    h33 = models.CharField(verbose_name="Heading Text 3", max_length=50)
    p3 = models.TextField(verbose_name="Paragraph Text 3")

    def __str__(self):
        return " "
