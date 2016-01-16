from rest_framework import serializers
from hunter_bank.models import Offer, SCORING_POINT


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
