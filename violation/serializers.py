from rest_framework import serializers
from violation.models import Violation


class ViolationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ['time']
