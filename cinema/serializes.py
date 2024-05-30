from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get(
            "duration",
            instance.duration
        )
        instance.save()
        return instance