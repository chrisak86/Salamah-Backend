from rest_framework.views import APIView
from ..models import FireStation
from ..serializers.fireStationSerializer import FireStationSerializer
from rest_framework.response import Response
from drf_spectacular.views import extend_schema, OpenApiParameter


@extend_schema(
        tags=['Departments']
    )
class FireStationPostView(APIView):
    serializer_class = FireStationSerializer
   
    def post(self, request):
        data=request.data
        serializer=FireStationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "FireStation created",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "FireStation not created",
                'data': serializer.errors,
                'success': False
            })
class FireStationGetView(APIView):
    @extend_schema(
        tags=['Departments']
    )

    def get(self, request):
        fire_station=FireStation.objects.all().order_by('id')
        serializer=FireStationSerializer(fire_station, many=True)
        return Response({
                'message': "FireStation list",
                'data': serializer.data,
                'success': True
            })
        
class FireStationPatchView(APIView):
    serializer_class = FireStationSerializer
    @extend_schema(
        tags=['Departments']
    )

    def patch(self, request):
        id = request.data.get('id')
        fire_station=FireStation.objects.get(id=id)
        serializer=FireStationSerializer(fire_station, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Fire Station updated",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "Fire Station not updated",
                'data': serializer.errors,
                'success': False
            })
