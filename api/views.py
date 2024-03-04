from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all() #listar elementos de un modelo.
    serializer_class = ProgrammerSerializer #serializar los datos de un modelo.