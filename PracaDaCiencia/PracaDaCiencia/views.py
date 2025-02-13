from .serializers import TecnicoSerializer  # Importa o serializer que criamos
from rest_framework import generics
from .models import Tecnico
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class CriarTecnico(generics.CreateAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tecnico

@csrf_exempt #Permite não usar tokens   
def filtrar_tecnicos(request): #Para filtrar
    if request.method == 'POST':
        try:
            dados = json.loads(request.body) #Transforma a requisiçaõ bruta em um dicionário python     
            name = dados.get('nome')
            email = dados.get('email')
            
            filtros = {}
            if name:
                filtros['name__icontains'] = name #Procura nome case insensitive
            if email:
                filtros['email__icontains'] = email #msm
            
            tecnicos = Tecnico.objects.filter(**filtros) #Filtra pelo dicionário descompactado
            resultado = list(tecnicos.values('name', 'email'))
            
            return JsonResponse({'tecnicos': resultado}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Formato JSON inválido'}, status=400)
    return JsonResponse({'erro': 'Método não permitido'}, status=405)

