from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import HTMLTagPluginModel, HeroChildPlugin
from .forms import HTMLTagPluginForm


@plugin_pool.register_plugin
class HTMLTagPlugin(CMSPluginBase):
    model = HTMLTagPluginModel
    form = HTMLTagPluginForm
    name = _("Tag - Text")
    render_template = "cms/plugins/html_tag_plugin.html"
    cache = False
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


@plugin_pool.register_plugin
class HeroSectionParentCMSPlugin(CMSPluginBase):
    render_template = 'cms/plugins/herosection/parent.html'
    name = 'Hero Parent'
    allow_children = True
    child_classes = ['HeroSectionChildCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class HeroSectionChildCMSPlugin(CMSPluginBase):
    render_template = 'cms/plugins/herosection/child.html'
    name = 'Hero Child'
    model = HeroChildPlugin
    require_parent = True
    parent_classes = ['HeroSectionParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(HeroSectionChildCMSPlugin, self).render(context, instance, placeholder)
        return context
