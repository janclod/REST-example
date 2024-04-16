from server.models import Municipality
from server.serializers import MunicipalitySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MunicipalityList(APIView):
    """
    List all municipalities, or create a new snippet.
    """
    def get(self, request, format=None):
        municipalities = Municipality.objects.all()
        serializer = MunicipalitySerializer(municipalities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MunicipalitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MunicipalityDetail(APIView):
    """
    Retrieve, update or delete a municipality instance.
    """
    def get_object(self, pk):
        try:
            return Municipality.objects.get(pk=pk)
        except Municipality.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        municipality = self.get_object(pk)
        serializer = MunicipalitySerializer(municipality)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        municipality = self.get_object(pk)
        serializer = MunicipalitySerializer(municipality, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        municipality = self.get_object(pk)
        municipality.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)