from rest_framework_gis.serializers import GeoFeatureModelSerializer
from models import Municipality

class LocationSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Municipality
        geo_field = "multipolygon"
