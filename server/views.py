from server.models import Municipality
from server.serializers import MunicipalitySerializer
from rest_framework import generics

class MunicipalityList(generics.ListAPIView):
    """
    List all municipalities, or create a new municipality.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

class MunicipalityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a municipality instance.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer