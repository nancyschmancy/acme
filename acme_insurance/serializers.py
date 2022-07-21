import re

from localflavor.us.us_states import STATES_NORMALIZED
from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    # add model properties
    base_premium = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_term_premium = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_term_discounts = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_term_fees = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_monthly_premium = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_monthly_discounts = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    total_monthly_fees = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'
        write_only_fields = ('effective_date', 'has_cancelled', 'owns_property', 'state', 'zip')

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
