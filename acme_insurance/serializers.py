from localflavor.us.us_states import STATES_NORMALIZED
from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.Serializer):
    effective_date = serializers.DateField()
    has_cancelled = serializers.BooleanField()
    owns_property = serializers.BooleanField()
    state = serializers.CharField()
    zip_code = serializers.CharField(max_length=10)

    @staticmethod
    def validate_state(value):
        """ Checks state value against normalized state data """

        if value.lower() not in STATES_NORMALIZED:
            raise serializers.ValidationError('{} is not a valid US state'.format(value))
        return STATES_NORMALIZED[value]

    # @staticmethod
    # def validate_zip_code(value):
    #     if valu

    def create(self, validated_data):
        return Quote.objects.create(validated_data)

    def update(self, instance, validated_data):
        """ Not implemented in this API """

        return instance
