from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import HTMLTagPluginModel
from .forms import HTMLTagPluginForm

class HTMLTagPlugin(CMSPluginBase):
    model = HTMLTagPluginModel
    form = HTMLTagPluginForm
    name = _("Tag - Text")
    render_template = "cms/plugins/html_tag_plugin.html"
    cache = False
    allow_children = True
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'tag',
                'content',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

plugin_pool.register_plugin(HTMLTagPlugin)
