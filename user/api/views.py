from ..models import Location, Position, Organization
from . import serializers
from . import pagination
from rest_framework import generics, status, filters
from rest_framework.serializers import ValidationError
from rest_framework.response import Response


class LocationListView(generics.ListAPIView):

    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['location_code',
                       'location_name', 'start_date', 'end_date']
    search_fields = ['location_code',
                     'location_name', 'start_date', 'end_date']

    def get_queryset(self):
        queryset = Location.objects.all()
        location_code = self.request.query_params.get('location_code', None)
        ordering = self.request.query_params.get('ordering', None)
        location_name = self.request.query_params.get('location_name', None)
        if location_code is not None:
            queryset = queryset.filter(
                location_code__icontains=str(location_code))
        if location_name is not None:
            queryset = queryset.filter(
                location_name__icontains=str(location_name))
        if ordering is not None:
            queryset = queryset.order_by(ordering)

        return queryset


class LocationCreateView(generics.CreateAPIView):

    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def create(self, request, *args, **kwargs):
        super(LocationCreateView, self).create(request, args, kwargs)
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully Created',
                    'result': request.data
                    }
        return Response(response)


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def retrieve(self, request, *args, **kwargs):
        super(LocationDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully retrieved',
                    'result': data}

        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(LocationDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(LocationDetailView, self).delete(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully deleted',
                    'result': data}

        return Response(response)

    def put(self, request, *args, **kwargs):
        super(LocationDetailView, self).put(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)


class PositionListView(generics.ListAPIView):

    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['Position_code',
                       'Position_name', 'organization_id', 'start_date', 'end_date']
    search_fields = ['Position_code',
                     'Position_name', 'organization_id', 'start_date', 'end_date']

    def get_queryset(self):
        queryset = Position.objects.all()
        position_code = self.request.query_params.get('position_code', None)
        ordering = self.request.query_params.get('ordering', None)
        position_name = self.request.query_params.get('position_name', None)
        if position_code is not None:
            queryset = queryset.filter(
                position_code__icontains=str(position_code))
        if position_name is not None:
            queryset = queryset.filter(
                position_name__icontains=str(position_name))
        if ordering is not None:
            queryset = queryset.order_by(ordering)

        return queryset


class PositionCreateView(generics.CreateAPIView):

    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer

    def create(self, request, *args, **kwargs):
        super(PositionCreateView, self).create(request, args, kwargs)
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully Created',
                    'result': request.data
                    }
        return Response(response)


class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PositionDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully retrieved',
                    'result': data}

        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PositionDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)

    def delete(self, request, *args, **kwargs):
        cek_key = self.kwargs.get('pk')
        cek_nilai = Organization.objects.filter(organization_id=int(cek_key))
        if cek_nilai.exists():
            raise ValidationError(
                'This data has relation with other table, remove it first')
        super(PositionDetailView, self).delete(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully deleted',
                    'result': data}

        return Response(response)

    def put(self, request, *args, **kwargs):
        super(PositionDetailView, self).put(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)


class OrganizationListView(generics.ListAPIView):

    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['organization_code',
                       'organization_name', 'organization_id', 'start_date', 'end_date']
    search_fields = ['organization_code',
                     'organization_name', 'organization_id', 'start_date', 'end_date']

    def get_queryset(self):
        queryset = Organization.objects.all()
        organization_code = self.request.query_params.get(
            'organization_code', None)
        ordering = self.request.query_params.get('ordering', None)
        organization_name = self.request.query_params.get(
            'organization_name', None)
        if organization_code is not None:
            queryset = queryset.filter(
                organization_code__icontains=str(organization_code))
        if organization_name is not None:
            queryset = queryset.filter(
                organization_name__icontains=str(organization_name))
        if ordering is not None:
            queryset = queryset.order_by(ordering)

        return queryset


class OrganizationCreateView(generics.CreateAPIView):

    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer

    def create(self, request, *args, **kwargs):
        super(OrganizationCreateView, self).create(request, args, kwargs)
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully Created',
                    'result': request.data
                    }
        return Response(response)


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer

    def retrieve(self, request, *args, **kwargs):
        super(OrganizationDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully retrieved',
                    'result': data}

        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(OrganizationDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)

    def delete(self, request, *args, **kwargs):
        cek_key = self.kwargs.get('pk')
        cek_nilai = Location.objects.filter(location_id=int(cek_key))
        if cek_nilai.exists():
            raise ValidationError(
                'This data has relation with other table, remove it first')
        super(OrganizationDetailView, self).delete(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully deleted',
                    'result': data}

        return Response(response)

    def put(self, request, *args, **kwargs):
        super(OrganizationDetailView, self).put(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Succesfully updated',
                    'result': data}

        return Response(response)
