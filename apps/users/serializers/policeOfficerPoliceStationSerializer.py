from rest_framework import serializers
from ..models import PoliceOfficerPoliceStaion

class PoliceOfficerPoliceStaionSerializer(serializers.ModelSerializer):
    class Meta:
        model=PoliceOfficerPoliceStaion
        fields='__all__'

    