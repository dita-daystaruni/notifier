from rest_framework import serializers
from .models import Semester, SemesterEvent


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"
        read_only_fields = ["__all__"]


class SemesterEvenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterEvent
        fields = "__all__"
        read_only_fields = ["__all__"]
