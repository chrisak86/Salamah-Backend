from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers.custom_user_serializers import ModelLogsSerializer
from ..serializers.ticketSerializer import TicketSerializer
from ..models import PoliceOfficerPoliceStaion, Ticket
from drf_spectacular.views import extend_schema
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from ..models import CustomUser


class TicketView(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=['Tickets']
    )
    def post(self, request):
        user = request.user
        request_data = request.data
        data={
            'user_id': user.id,
            'user_name': user.first_name,
            'eta': request_data.get('eta'),
            'distance': request_data.get('distance'),
            'police_station_id': request_data.get('police_station_id'),
            'hospital_id': request_data.get('hospital_id'),
            'firetruck_id': request_data.get('firetruck_id'),
            'hospital_name': request_data.get('hospital_name'),
            'police_station_name': request_data.get('police_station_name'),
            'fire_station_name': request_data.get('fire_station_name'),
            'attend_id': request_data.get('attend_id'),
            'user_lat': request_data.get('user_lat'),
            'user_long': request_data.get('user_long'),
            'dest_lat': request_data.get('dest_lat'),
            'dest_long': request_data.get('dest_long'),
            'completed': request_data.get('completed'),
            'type_choice': request_data.get('type_choice'),           
        }
        serializer=TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                'message': 'Ticket Posted',
                'data': serializer.data,
                'success': True
            })
        return Response({
                'message': 'Ticket not Posted',
                'data': serializer.errors,
                'success': True
            })
    
class PatchTicket(APIView):
    serializer_class = TicketSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    @extend_schema(
        tags=['Tickets']
    )
    def patch(self, request):
        try:
            ticket = Ticket.objects.get(id=request.data.get('id'))
        except Ticket.DoesNotExist:
            return Response({
                'message': 'Ticket not found',
                'success': False
            })
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Ticket updated successfully',
                'data': serializer.data,
                'success': True
            })
        
        return Response({
            'message': 'Invalid data',
            'errors': serializer.errors,
            'success': False
        })



class GetTicket(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer
    @extend_schema(
        tags=['Tickets']
    )

    def post(self, request):
        user = request.user
        
        data = request.data.get('type_choice')
        
        if data not in ['AMBULANCE', 'FIRETRUCK', 'ACCIDENT']:
            return Response({
                'message': 'Type choice is not valid',
                'success': False
            })
        
        tickets = Ticket.objects.filter(
            user_id=user,
            completed=False,
            type_choice=data
        )
        
        serializer = TicketSerializer(tickets, many=True)
        
        return Response({
            'message': f'Get {data}',
            'data': serializer.data, 
            'success': True
        })
class PoliceTicket(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=['Tickets']
    )
    def get(self, request):
        user=request.user
        user_id=user.id
        ticket=Ticket.objects.filter(
            attend_id=user_id,
            completed=False
        )
        
        if ticket:
            serializer=TicketSerializer(ticket, many=True)
            return Response({
                'message': 'tickets by user',
                'data': serializer.data, 
                'success': True
            })

       
        
        user_profile = CustomUser.objects.get(id=user_id)
        police_stations = PoliceOfficerPoliceStaion.objects.filter(user=user_profile).values_list('police_station_id', flat=True)

        if police_stations.exists():
            tickets = Ticket.objects.filter(police_station_id__in=police_stations, completed=False)
            
            if tickets.exists():
                serializer = TicketSerializer(tickets, many=True)
                return Response({
                    'message': 'Tickets assigned to police stations',
                    'data': serializer.data,
                    'success': True
                })

        return Response({
            'message': 'No tickets available',
            'success': False
        })
    

class AllTickets(APIView):
    serializer_class = TicketSerializer
    @extend_schema(
        tags=['Tickets']
    )
    def get(self, request):
        tickets=Ticket.objects.all()
        serializer=TicketSerializer(tickets, many=True)
        return Response({
            'message': 'Tickets Success',
            'data': serializer.data,
            'success': True
        })
    
class FalseTicketsView(APIView):
    @extend_schema(
        tags=['Tickets']
    )
    def get(self, request):
        false_tickets=Ticket.objects.filter(completed=False)
        serializer=TicketSerializer(false_tickets, many= True)
        return Response({
            'message': 'False Tickets',
            'data': serializer.data,
            'success': True
        })
    

class CreateModelLogView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ModelLogsSerializer

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        
        serializer = ModelLogsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Log created successfully",
                "success": True
            })
        return Response({
            "data": None,
            "message": serializer.errors,
            "success": False
        })
