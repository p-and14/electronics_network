from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from network import serializers
from network.filters import OrganizationFilter
from network.models import Organization


class OrganizationListView(generics.ListAPIView):
    model = Organization
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrganizationListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_class = OrganizationFilter
    ordering = ["level", "title"]
    search_fields = ["contacts__address__city"]


class OrganizationCreateView(generics.CreateAPIView):
    model = Organization
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrganizationSerializer


class OrganizationView(generics.RetrieveUpdateDestroyAPIView):
    model = Organization
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrganizationSerializer

    def perform_destroy(self, instance):
        Organization.objects.filter(supplier=instance.pk).update(supplier=None)
        instance.delete()
