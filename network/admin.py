from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network import models


@admin.action(description="Обнулить задолженность")
def cancel_the_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "level", "contacts_city", "supplier_link", "debt_to_supplier")
    list_display_links = ("id", "title")
    list_filter = ("contacts__address__city", )
    list_select_related = ('contacts',)
    actions = [cancel_the_debt]

    @admin.display(description="City")
    def contacts_city(self, obj: models.Organization):
        return obj.contacts.address.city if obj.contacts else None

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                u'<b><a href="{0}">{1}</a></b>'.format(
                    reverse("admin:network_organization_change", args=(obj.supplier.pk,)),
                    obj.supplier)
            )
        else:
            return obj.supplier

    supplier_link.allow_tags = True
    supplier_link.admin_order_field = 'supplier'
    supplier_link.short_description = "Поставщик"


admin.site.register(models.Address)
admin.site.register(models.Contact)
admin.site.register(models.Product)
admin.site.register(models.Organization, OrganizationAdmin)
