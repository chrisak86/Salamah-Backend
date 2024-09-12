import ast
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.policeOfficerPoliceStationSerializer import PoliceOfficerPoliceStaionSerializer
from ..models import PoliceOfficerPoliceStaion, CustomUser
from ...departments.models import PoliceStation
from drf_spectacular.views import extend_schema


class OfficerPoliceStaionView(APIView):
    serializer_class = PoliceOfficerPoliceStaionSerializer
    @extend_schema(
        tags=['Police Station Assigning']
    )

    def post(self, request):
        user=request.data.get('user')
        user=CustomUser.objects.get(id=user)
        if user.user_type == "POLICE":
            police_stations = request.data.get('police_station')
            police_stations = ast.literal_eval(police_stations)
            print(police_stations)
            for police_station in police_stations:
                data={
                    'user': request.data.get('user'),
                    'police_station': police_station
                }
                serializer=PoliceOfficerPoliceStaionSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(police_station)
                    return Response({
                    'message': "Police Station not Assigned/serializer error",
                    'data': serializer.errors,
                    'success': True
                })
            return Response({
                        'message': "Police Station Assigned",
                        'data': {'data':serializer.data, 'police_stations': police_stations},
                        'success': True
                    })
        return Response({
                    'message': "user is not police officer",
                    'success': False
                })
    
    
