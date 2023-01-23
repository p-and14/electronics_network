from django.urls import path

from network import views

urlpatterns = [
    path("organization/list", views.OrganizationListView.as_view(), name="organization_list"),
    path("organization/create", views.OrganizationCreateView.as_view(), name="organization_create"),
    path("organization/<int:pk>", views.OrganizationView.as_view(), name="organization_pk"),
]