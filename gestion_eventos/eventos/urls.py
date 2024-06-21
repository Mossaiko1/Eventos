from . import views
from django.urls import path, include
from rest_framework import routers
from .api import EventViewSet

router = routers.DefaultRouter()
router.register('', EventViewSet, 'eventos')

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('eliminar/<int:event_id>/', views.confirm_delete_event, name='confirm_delete_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('api/', include(router.urls)),
]
