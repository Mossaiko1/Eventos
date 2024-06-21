from . import views
from django.urls import path, include
from rest_framework import routers
from .api import ParticipantViewSet

router = routers.DefaultRouter()
router.register('', ParticipantViewSet, 'participantes')

urlpatterns = [
    path('', views.participant_list, name='participant_list'),
    path('edit/<int:participant_id>/', views.edit_participant, name='edit_participant'),
    path('delete/<int:participant_id>/', views.confirm_delete_participant, name='confirm_delete_participant'),
    path('delete/<int:participant_id>/', views.delete_participant, name='delete_participant'),
    path('change_status/', views.change_status, name='change_status'),
    path('api/', include(router.urls)),
]