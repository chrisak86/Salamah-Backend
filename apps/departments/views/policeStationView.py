from rest_framework.views import APIView
from ..models import PoliceStation
from ..serializers.policeStationSerializer import PoliceStationSerializer
from rest_framework.response import Response
from drf_spectacular.views import extend_schema, OpenApiParameter
from ...users.models import CustomUser


@extend_schema(
        tags=['Departments']
    )

class PoliceStationPostView(APIView):
    serializer_class = PoliceStationSerializer

    def post(self, request):
        data=request.data
        serializer=PoliceStationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Police station created",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "Police station not created",
                'data': serializer.errors,
                'success': False
            })
class PoliceStationGetView(APIView):
    @extend_schema(
        tags=['Departments']
    )

    def get(self, request):
        polic_station=PoliceStation.objects.all().order_by('id')
        print(polic_station)
        serializer=PoliceStationSerializer(polic_station, many=True)
        return Response({
                'message': "Police station list",
                'data': serializer.data,
                'success': True
            })
        
class PoliceStationPatchView(APIView):
    serializer_class = PoliceStationSerializer
    @extend_schema(
        tags=['Departments']
    )

    def patch(self, request):
        id = request.data.get('id')
        polic_station=PoliceStation.objects.get(id=id)
        serializer=PoliceStationSerializer(polic_station, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Police station updated",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "Police station not updated",
                'data': serializer.errors,
                'success': False
            })


class Delete(APIView):
    def post(self, request):
        # Flush (delete) all entries in the table
        CustomUser.objects.all().delete()
        return Response({"message": "All records deleted"}, status=200)