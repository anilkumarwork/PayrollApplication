from rest_framework import serializers
from .models import AbleDesignation


class AbleDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbleDesignation
        fields = '__all__'
