import logging

logger = logging.getLogger('django_oembed')

from django.contrib import admin

from django_oembed.models import *
from django_oembed.forms import *

from django_oembed.util import remove_from_fieldsets

class OembedAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'modify_date', )
    search_fields = ('title', 'slug', 'description' )
    ordering = ('title', )

    actions_on_top = False
    actions_on_bottom = True

    def get_fieldsets(self, request, obj=None):
        "Hook for specifying fieldsets for the add form."
        
        original_fieldsets = super(OembedAdmin, self).get_fieldsets(request, obj)
        if not obj:
            # We're adding stuff
            
            return original_fieldsets
        else:
            # Organise this stuff a bit
            remove_from_fieldsets(original_fieldsets, ('title', 'slug', 'description'))
            
            return (
                        (None, {
                            'fields': ('title', 'slug', 'description',)
                        }),
                        ('Content', original_fieldsets[0][1])
                   )

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            # We're adding stuff
            logger.debug('Rendering add form for %s' % self.model)
            return self.add_form
        else:
            logger.debug('Rendering normal form.')
            return super(OembedAdmin, self).get_form(request, obj, **kwargs)
    
    def get_readonly_fields(self, request, obj=None, **kwargs):
        """ No preview for new items. """
        
        if not obj:
            return ()
        else:
            readonly = ['url', ]
            
            if obj.thumbnail_url:
                readonly.append('get_thumbnail')
            
            if obj.html:
                readonly.append('get_html')
            
            if obj.provider_name:
                readonly.append('get_provider')
            
            if obj.author_name:
                readonly.append('get_author')
            
            return readonly
            
    def get_html(self, obj):
        """ Get HTML to display the current object properly. This
            method should be defined in child classes. """
        
        if obj.html:
            return obj.html
        
        return None
    get_html.short_description = 'preview'
    get_html.allow_tags = True

    def get_provider(self, obj):
        if obj.provider_name:
            if obj.provider_url:
                return u'<a href="%s">%s</a>' % \
                    (obj.provider_url, obj.provider_name)
            else:
                return obj.provider_name
        
        return None
    get_provider.short_description = 'provider'
    get_provider.allow_tags = True
    
    def get_author(self, obj):
        if obj.author_name:
            if obj.author_url:
                return u'<a href="%s">%s</a>' % \
                    (obj.author_url, obj.author_name)
            else:
                return obj.author_name
        
        return None
    get_author.short_description = 'author'
    get_author.allow_tags = True
            
    def get_thumbnail(self, obj):
        if obj.thumbnail_url:
            assert obj.title
            assert obj.thumbnail_width
            assert obj.thumbnail_height
            
            return '<img src="%s" alt="%s" width="%d" height="%d"/>' % \
                (obj.thumbnail_url, obj.title, obj.thumbnail_width, obj.thumbnail_height)
        
        return None
    get_thumbnail.short_description = 'thumbnail'
    get_thumbnail.allow_tags = True
            

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
