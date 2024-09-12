from rest_framework import serializers
from ..models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField()
    class Meta:
        model=Hospital
        fields=['id', 'status', 'location', 'longitude', 'latitude','hospital_name']