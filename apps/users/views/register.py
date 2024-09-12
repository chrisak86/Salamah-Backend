from rest_framework.views import APIView
from drf_spectacular.views import extend_schema
from ..models import CustomUser
from rest_framework.response import Response
from ..serializers.custom_user_serializers import CustomUserSerializers
from django.contrib.auth.hashers import check_password
from django.urls import URLPattern
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Ticket





class RegisterViews(APIView):
    serializer_class = CustomUserSerializers
    @extend_schema(
        tags=['auth']
    )
    def post(self, request):
        email=request.data.get('email')
        existing_user=CustomUser.objects.filter(email=email).exists()
        if existing_user:
            return Response("user exists")

        serializer=CustomUserSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'message': 'User Created',
                    'data': serializer.data,
                    'status':  True
                
                })
        return Response({
                    'message': 'User not Created',
                    'data': serializer.errors,
                    'status':  False
                
                })
    
class UserLoginView(APIView):
    serializer_class = CustomUserSerializers
    @extend_schema(
        tags=['auth']
    )
    def post(self, request):
      
        email = request.data.get('email')
        password = request.data.get('password')

        existing_user = CustomUser.objects.filter(email=email).first()

        if existing_user:
            if existing_user.check_password(password):
                token_serializer = TokenObtainPairSerializer(data={
                    'email': email,
                    'password': password
                })
                if token_serializer.is_valid():

                    serializer = CustomUserSerializers(existing_user)
                    return Response({
                    'message': 'Logged in',
                    'auth': token_serializer.validated_data['access'],
                    'data': serializer.data,
                    'status': True
                    })
                return Response({
                    'message': 'Unable to generate token',
                    'status': False
                })
            return Response({
                'message': 'Password is not valid',
                'status': False
            })

        return Response({
            'message': 'User does not exist',
            'status': False
        })
    

class UserPatchView(APIView):
    serializer_class = CustomUserSerializers
    @extend_schema(
        tags=['auth']
    )
    
    def patch(self, request):
        email=request.data.get('email')
        
        user=CustomUser.objects.get(email=email)
        
        serializer=CustomUserSerializers(user, data=request.data, partial=True)
        if serializer.is_valid():
             password = request.data.get('password')
             if password:
                user.set_password(password)
                user.save()
             else:
                serializer.save()
             return Response({
                    'message': 'updated user',
                    'data': serializer.data,
                    'status':  True
                
                })
        else:
            return Response({
                    'message': 'User not updated',
                    'data': serializer.errors,
                    'status':  True
                
                })
        
class PoliceOfficerView(APIView):
    serializer_class = CustomUserSerializers
    @extend_schema(
        tags=['auth']
    )
    def get(self, request):
        police_officer=CustomUser.objects.filter(user_type="POLICE").order_by('id')
        serializer=CustomUserSerializers(police_officer, many=True)
        return Response({
                'message': "Police Officer list",
                'data': serializer.data,
                'success': True
            })


class GetUserAPIView(APIView):
    serializer_class = CustomUserSerializers
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=['auth']
    )
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializers(user)
        return Response({
            'data': serializer.data,
            'message': 'user retrieved successfully',
            'success': True
        })
    
