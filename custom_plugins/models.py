from django.db import models
from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField


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