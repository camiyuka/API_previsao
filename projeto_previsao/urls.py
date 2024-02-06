from django.contrib import admin
from django.urls import path
from app_previsao.views import PrevisaoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('previsao/', PrevisaoViewSet.as_view({'get': 'list', 'post': 'create'})),  # List and Create endpoints
    path('previsao/<int:pk>/', PrevisaoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'})),  # Retrieve, Update, and Delete endpoints
]
