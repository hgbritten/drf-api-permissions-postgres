from rest_framework import serializers
from .models import Climb


class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "difficulty", "created_at")
        model = Climb
