from rest_framework.views import APIView
from ..models import Hospital
from ..serializers.hospitalSerializer import HospitalSerializer
from rest_framework.response import Response
from drf_spectacular.views import extend_schema, OpenApiParameter


@extend_schema(
        tags=['Departments']
    )

class HospitalPostView(APIView):
    serializer_class = HospitalSerializer

    def post(self, request):
        data=request.data
        serializer=HospitalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Hospital created",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "Hospital not created",
                'data': serializer.errors,
                'success': False
            })
class HospitalGetView(APIView):
    @extend_schema(
        tags=['Departments']
    )

    def get(self, request):
        hospital=Hospital.objects.all().order_by('id')
        serializer=HospitalSerializer(hospital, many=True)
        return Response({
                'message': "Hospital list",
                'data': serializer.data,
                'success': True
            })
        
class HospitalPatchView(APIView):
    serializer_class = HospitalSerializer
    @extend_schema(
        tags=['Departments']
    )

    def patch(self, request):
        id = request.data.get('id')
        hospital=Hospital.objects.get(id=id)
        serializer=HospitalSerializer(hospital, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Hospital updated",
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': "Hospital not updated",
                'data': serializer.errors,
                'success': False
            })
