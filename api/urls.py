from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()#crear un enrutador.
router.register(r'programmers', views.ProgrammerViewSet) #url para acceder a la vista de programadores.

urlpatterns=[
    path('', include(router.urls)), #incluye las urls del enrutador.
]