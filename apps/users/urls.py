from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.register import *
from .views.policeOfficerPoliceStation import OfficerPoliceStaionView
from .views.ticketView import *


auth_urls = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', RegisterViews.as_view(), name='Register'),
    path('token/', TokenObtainPairView.as_view(), name="token"),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('update-user/', UserPatchView.as_view(), name='update-user'),
    path('police-officer/', PoliceOfficerView.as_view(), name='police-officer'),
    path('get-user/', GetUserAPIView.as_view(), name='get-user'),

]

other_urls=[
    path('assign-police-station/', OfficerPoliceStaionView.as_view(), name='Assign Police Station'),
    path('ticket/', TicketView.as_view(), name='ticket'),
    path('get-ticket/', GetTicket.as_view(), name='get-ticket'),
    path('police-ticket/', PoliceTicket.as_view(), name='tickets-assigning'),
    path('update-ticket/', PatchTicket.as_view(), name='update-ticket'),
    path('all-ticket/', AllTickets.as_view(), name='all-ticket'),
    path('pending-ticket/', FalseTicketsView.as_view(), name='pending-ticket'),

]



urlpatterns = [
   *auth_urls, *other_urls
]