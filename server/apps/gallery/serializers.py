from django.conf import settings
from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, instance):
        return f"{settings.MEDIA_ROOT}/{instance.thumbnail}"

    class Meta:
        model = Gallery
        fields = (
            "title",
            "url",
            "thumbnail",
        )
