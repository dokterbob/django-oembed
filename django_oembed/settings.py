from django.conf import settings

OEMBED_MAX_WIDTH = getattr(settings, 'OEMBED_MAX_WIDTH', None)
OEMBED_MAX_HEIGHT = getattr(settings, 'OEMBED_MAX_HEIGHT', None)
