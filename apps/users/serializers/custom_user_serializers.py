from rest_framework import serializers
from ..models import CustomUser, ModelLogs, PoliceOfficerPoliceStaion


class CustomUserSerializers(serializers.ModelSerializer):
    police_station = serializers.SerializerMethodField()
    class Meta:
        model=CustomUser
        fields=['id','email','first_name','password', 'civil_id', 'gender', 'user_type', 'is_approved', 'is_online', 'police_station']
        extra_kwargs={'password': {"write_only": True,"required": True},
                       'email': {'required': True},
                        }
    
    def get_police_station(self, obj):
        # Check if the user is a police officer
        if obj.user_type == 'POLICE':
            # Fetch the PoliceStation IDs linked to the police officer
            police_station_ids = PoliceOfficerPoliceStaion.objects.filter(user=obj).values_list('police_station_id', flat=True)
            return list(police_station_ids)
        return None

    def create(self, validated_data):
        validated_data.pop('police_station', None)
        user = CustomUser.objects.create_user(
        email=validated_data['email'],
        password=validated_data['password'],
        first_name=validated_data.get('first_name'),
        civil_id=validated_data.get('civil_id'),
        gender=validated_data.get('gender'),
        user_type=validated_data.get('user_type'),
        is_approved=validated_data.get('is_approved', False),
        is_online=validated_data.get('is_online', False)
    )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ModelLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLogs
        fields = "__all__"

    