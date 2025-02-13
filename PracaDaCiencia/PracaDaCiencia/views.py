from rest_framework.views import APIView  # Importa a classe base para criar a API
from rest_framework.response import Response  # Permite retornar respostas JSON
from rest_framework import status  # Importa os códigos HTTP (200, 201, 400, etc.)
from .serializers import TecnicoSerializer  # Importa o serializer que criamos
from rest_framework import generics
from .models import Tecnico

class CriarTecnico(generics.CreateAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
