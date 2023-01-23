from rest_framework import serializers

from network.models import Organization, Contact, Product, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrganizationListSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    contacts = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ("id", "created", "debt_to_supplier")

    def get_level(self, obj):
        return Organization.Level.choices[obj.level - 1][1]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ("id", "created", "debt_to_supplier")

    def validate(self, attrs):
        if attrs.get("level") != Organization.Level.factory:
            if not attrs.get("supplier"):
                raise serializers.ValidationError({"supplier": "required field"})
        return attrs
