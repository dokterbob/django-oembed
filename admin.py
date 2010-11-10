from django.contrib import admin

from django_oembed.models import *
from django_oembed.forms import *

class OembedAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'modify_date', )
    search_fields = ('title', 'slug', 'description' )
    ordering = ('title', )

    actions_on_top = False
    actions_on_bottom = True


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