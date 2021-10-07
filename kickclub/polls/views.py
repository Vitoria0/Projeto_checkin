from rest_framework import generics
from .models import custumer
from .serializers import custumerserializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("Você está dentro de polls index")

class custumerlist(generics.ListCreateAPIView):
    queryset = custumer.objects.all()
    serializer_class = custumerserializer
