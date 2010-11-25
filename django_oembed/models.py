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

    thumbnail_url = models.URLField(blank=True, verify_exists=True, editable=False)
    thumbnail_width = models.SmallIntegerField(blank=True, null=True, editable=False)
    thumbnail_height = models.SmallIntegerField(blank=True, null=True, editable=False)

    provider_name = models.CharField(blank=True, max_length=255, editable=False)
    provider_url = models.CharField(blank=True, max_length=255, editable=False)

    author_name = models.CharField(blank=True, max_length=255, editable=False)
    author_url = models.URLField(blank=True, verify_exists=False, editable=False)


class Link(OembedAbstractBase):
    pass


class EmbeddedRich(OembedAbstractBase):
    html = models.TextField(blank=True, editable=False)
    width = models.SmallIntegerField(blank=True, null=True, editable=False)
    height = models.SmallIntegerField(blank=True, null=True, editable=False)


class EmbeddedVideo(OembedAbstractBase):
    html = models.TextField(blank=True, editable=False)
    width = models.SmallIntegerField(blank=True, null=True, editable=False)
    height = models.SmallIntegerField(blank=True, null=True, editable=False)

    duration = models.SmallIntegerField(blank=True, null=True, editable=False)


class EmbeddedPhoto(OembedAbstractBase):
    width = models.SmallIntegerField(blank=True, null=True, editable=False)
    height = models.SmallIntegerField(blank=True, null=True, editable=False)
