from django.urls import path
from .views.policeStationView import PoliceStationPostView, PoliceStationGetView, PoliceStationPatchView, Delete
from .views.hospitalView import HospitalPostView, HospitalGetView, HospitalPatchView
from .views.fireStationView import FireStationPostView, FireStationGetView, FireStationPatchView

HOSPITAL = [
    path('add-hospital/', HospitalPostView.as_view(), name='Hospital'),
    path('list-hospital/', HospitalGetView.as_view(), name='Hospital'),
    path('update-hospital/', HospitalPatchView.as_view(), name='Hospital'),
]

POLICE_STATION = [
    path('add-police-station/', PoliceStationPostView.as_view(), name='Police Station'),
    path('list-police-station/', PoliceStationGetView.as_view(), name='Police Station'),
    path('update-police-station/', PoliceStationPatchView.as_view(), name='Police Station'),
    
]

FIRE_STATION = [
    path('add-fire-station/', FireStationPostView.as_view(), name='Police Station'),
    path('list-fire-station/', FireStationGetView.as_view(), name='Police Station'),
    path('update-fire-station/', FireStationPatchView.as_view(), name='Police Station'),
    
]

urlpatterns = [
    *POLICE_STATION, *FIRE_STATION, *HOSPITAL,
    # path('delete/', Delete.as_view(), name='Police Station'),

]
