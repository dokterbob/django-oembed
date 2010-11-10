import logging

logger = logging.getLogger('django_oembed')

from django.contrib import admin

from django_oembed.models import *
from django_oembed.forms import *


class OembedAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'modify_date', )
    search_fields = ('title', 'slug', 'description' )
    ordering = ('title', )

    actions_on_top = False
    actions_on_bottom = True

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            # We're adding stuff
            logger.debug('Rendering add form for %s' % self.model)
            return self.add_form
        else:
            logger.debug('Rendering normal form.')
            return super(OembedAdmin, self).get_form(request, obj, **kwargs)


class LinkAdmin(OembedAdmin):
    add_form = LinkAddForm
admin.site.register(Link, LinkAdmin)


class EmbeddedVideoAdmin(OembedAdmin):
    add_form = EmbeddedVideoAddForm

admin.site.register(EmbeddedVideo, EmbeddedVideoAdmin)


class EmbeddedPhotoAdmin(OembedAdmin):
    add_form = EmbeddedPhotoAddForm

admin.site.register(EmbeddedPhoto, EmbeddedPhotoAdmin)


class EmbeddedRichAdmin(OembedAdmin):
    add_form = EmbeddedRichAddForm

admin.site.register(EmbeddedRich, EmbeddedRichAdmin)