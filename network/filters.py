from django_filters import rest_framework, filters

from network.models import Organization


class OrganizationFilter(rest_framework.FilterSet):
    city = filters.CharFilter(
        field_name="contacts__address__city",
        lookup_expr="icontains"
    )

    class Meta:
        model = Organization
        fields = ["contacts"]
