from django import forms
from djangocms_attributes_field.widgets import AttributesWidget
from .models import HTMLTagPluginModel


class HTMLTagPluginForm(forms.ModelForm):
    class Meta:
        model = HTMLTagPluginModel
        fields = ["tag", "content", "attributes"]
        widgets = {
            "attributes": AttributesWidget,
        }