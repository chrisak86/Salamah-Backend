from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

swagger_urls = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

apps_urls=[
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.departments.urls')),


]

admin_urls=[
    path('admin/', admin.site.urls),

]

urlpatterns = [
    *swagger_urls, *apps_urls, *admin_urls

]

