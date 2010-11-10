from django.db import models

from metadata.models import DateAbstractBase, DescriptionAbstractBase, \
                            TitleAbstractBase, SlugAbstractBase


""" Most of the code below comes from: 
    http://github.com/dokterbob/django-metaphore/blob/master/metaphore/models.py 
"""

class OembedAbstractBase(TitleAbstractBase,
                         SlugAbstractBase,
                         DateAbstractBase,
                         DescriptionAbstractBase):
    """ Abstract base class for Oembed objects. """

    class Meta:
        abstract = True

    # Title is already in there

    url = models.URLField(verify_exists=True)

    thumbnail_url = models.URLField(blank=True, verify_exists=True)
    thumbnail_width = models.SmallIntegerField(blank=True, null=True)
    thumbnail_height = models.SmallIntegerField(blank=True, null=True)

    provider_name = models.CharField(blank=True, max_length=255)
    provider_url = models.CharField(blank=True, max_length=255)

    author_name = models.CharField(blank=True, max_length=255)
    author_url = models.URLField(blank=True, verify_exists=False)


class Link(OembedAbstractBase):
    pass


class EmbeddedRich(OembedAbstractBase):
    html = models.TextField(blank=True)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)


class EmbeddedVideo(OembedAbstractBase):
    html = models.TextField(blank=True)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)

    duration = models.SmallIntegerField(blank=True, null=True)


class EmbeddedPhoto(OembedAbstractBase):
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
