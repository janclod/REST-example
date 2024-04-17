from server.models import Municipality
from server.serializers import MunicipalitySerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework_gis.filters import InBBoxFilter


class MunicipalityList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all municipalities, or create a new municipality.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MunicipalityDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    Retrieve, update or delete a municipality instance.
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
