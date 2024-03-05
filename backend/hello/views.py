from rest_framework import generics

# ============================================================================ #
from .models import Hello
from .serializers import HelloSerializer


# Create your views here.


class HelloList(generics.ListAPIView):
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
