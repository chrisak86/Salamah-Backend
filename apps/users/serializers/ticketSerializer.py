from rest_framework import serializers
from ..models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields='__all__'
        extra_kwargs={'attend_id': {'required': False,"allow_null": True},
                      'hospital_id': {'required': False,"allow_null": True},
                      'police_station_id': {'required': False,"allow_null": True},
                      'firetruck_id': {'required': False,"allow_null": True},
                      'police_station_name': {'required': False,"allow_null": True},
                      'fire_station_name': {'required': False,"allow_null": True},
                      'hospital_name': {'required': False,"allow_null": True},
                      } 