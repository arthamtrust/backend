from typing import Literal, Union

from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "published_date",
        )


def post_validator(kind: Union[Literal["charity"], Literal["event"]]):
    def validator(value: str):
        if value != kind:
            raise serializers.ValidationError(
                f"{kind.capitalize()} post must have 'kind' as '{kind}'"
            )

    return validator


class CharityPostSerializer(PostSerializer):
    def validate(self, data):
        if "kind" in data and data["kind"] != "charity":
            raise serializers.ValidationError(
                "Charity post must have 'kind' as 'charity'"
            )
        data["kind"] = "charity"
        return super().validate(data)


class EventPostSerializer(PostSerializer):
    def validate(self, data):
        if "kind" in data and data["kind"] != "event":
            raise serializers.ValidationError(
                "Event post must have 'kind' as 'event'"
            )
        data["kind"] = "event"
        return super().validate(data)
