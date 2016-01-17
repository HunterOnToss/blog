from rest_framework import serializers
from hunter_bank.models import Offer, Client, SCORING_POINT


class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = ("ID",
                  "client_create",
                  "client_update",
                  "client_name",
                  "client_family",
                  "client_otchestvo",
                  "client_birthday",
                  "client_phone_number",
                  "client_passport_number",
                  "client_scoring_point",
                  )

    ID = serializers.IntegerField(read_only=True)
    client_create = serializers.DateTimeField(read_only=True)
    client_update = serializers.DateTimeField(read_only=True)
    client_name = serializers.CharField(required=True, max_length=48)
    client_family = serializers.CharField(required=True, max_length=48)
    client_otchestvo = serializers.CharField(required=True, max_length=48)
    client_birthday = serializers.DateField(required=True)
    client_phone_number = serializers.CharField(required=True, max_length=12)
    client_passport_number = serializers.IntegerField(required=True)
    client_scoring_point = serializers.ChoiceField(choices=SCORING_POINT)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class OfferSerializer(serializers.Serializer):
    class Meta:
        model = Offer
        fields = (
            "offer_create",
            "offer_update",
            "offer_rotation_begin",
            "offer_rotation_end",
            "offer_name",
            "offer_type",
            "offer_minimal_scoring_point",
            "offer_maximal_scoring_point",
            "offer_credit_organization",
        )

    pk = serializers.IntegerField(read_only=True)
    offer_create = serializers.DateTimeField(read_only=True)
    offer_update = serializers.DateTimeField(read_only=True)
    offer_rotation_begin = serializers.DateTimeField(read_only=True)
    offer_rotation_end = serializers.DateTimeField(read_only=True)
    offer_name = serializers.CharField(required=True, allow_blank=True, max_length=120)
    offer_type = serializers.ChoiceField(choices=Offer.TYPE_STATE)
    offer_minimal_scoring_point = serializers.ChoiceField(choices=SCORING_POINT)
    offer_maximal_scoring_point = serializers.ChoiceField(choices=SCORING_POINT)
    # offer_credit_organization = OfferCreditOrganizationSerializer(source="offer_credit_organization")
