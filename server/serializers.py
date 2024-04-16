from rest_framework_gis.serializers import GeoFeatureModelSerializer
from server.models import Municipality


class MunicipalitySerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Municipality
        geo_field = "coordinates"
        fields = ('id', 'name')
