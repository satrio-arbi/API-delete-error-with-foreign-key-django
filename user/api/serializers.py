from ..models import Location, Position, Organization
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_id', 'location_code',
                  'location_name', 'start_date', 'end_date']
        extra_kwargs = {'id': {'read_only': True}}


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_id', 'organization_code',
                  'organization_name', 'location_id', 'start_date', 'end_date']
        extra_kwargs = {'organization_id': {'read_only': True}}


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['position_id', 'position_code',
                  'position_name','organization_id', 'start_date', 'end_date']
        extra_kwargs = {'position_id': {'read_only': True}}
