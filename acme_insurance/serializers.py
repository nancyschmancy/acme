import re

from localflavor.us.us_states import STATES_NORMALIZED
from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    # add model properties
    total_term_premium = serializers.ReadOnlyField()
    total_term_discounts = serializers.ReadOnlyField()
    total_term_fees = serializers.ReadOnlyField()
    total_monthly_premium = serializers.ReadOnlyField()
    total_monthly_discounts = serializers.ReadOnlyField()
    total_monthly_fees = serializers.ReadOnlyField()

    class Meta:
        model = Quote
        fields = '__all__'
        read_only_fields = ('id', 'base_premium', 'cancelled_fee', 'volcano_fee', 'not_cancelled_discount',
                            'ownership_discount')

    def validate_effective_date(self, value):
        """ Check that request date is not in the past """
        # is this needed?

        return value

    def validate_zip_code(self, value):
        """ Checks that zip code follows the format XXXXX or XXXXX-XXXX """

        if not re.match("^[0-9]{5}(?:-[0-9]{4})?$", value):
            raise serializers.ValidationError('{} is not a valid US zip code format'.format(value))

        return value

    def validate_state(self, value):
        """ Checks request US state against normalized US state data """

        if value.lower() not in STATES_NORMALIZED:
            raise serializers.ValidationError('{} is not a valid US state'.format(value))

        return STATES_NORMALIZED[value.lower()]
