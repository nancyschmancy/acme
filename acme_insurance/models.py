import string
from django.db import models
from django.utils.crypto import get_random_string

ACTIVE_VOLCANO_STATES = {'AK', 'AZ', 'CA', 'CO', 'HI', 'ID', 'NV', 'NM', 'OR', 'UT', 'WA', 'WY'}
BASE_TERM_RATE = 59.94

## FEES
HAS_CANCELLED_FEE = 0.15
NEAR_VOLCANO_FEE = 0.25

## DISCOUNTS
NOT_CANCELLED_DISCOUNT = -0.10
OWNERSHIP_DISCOUNT = -0.20


def get_random_id():
    """ Generate a random 10 digit primary key in lieu of UUID """

    return get_random_string(10, allowed_chars=string.ascii_letters + string.digits)


class Quote(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=get_random_id, unique=True)
    effective_date = models.DateField()
    has_cancelled = models.BooleanField()
    owns_property = models.BooleanField()
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    base_premium = models.DecimalField(decimal_places=2, max_digits=10)

    # additional fees
    cancelled_fee = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    volcano_fee = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)

    # discounts
    not_cancelled_discount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    ownership_discount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)

    def save(self, *args, **kwargs):
        self.base_premium = BASE_TERM_RATE

        if self.has_cancelled:
            self.cancelled_fee = self.base_premium * HAS_CANCELLED_FEE
        else:
            self.not_cancelled_discount = self.base_premium * NOT_CANCELLED_DISCOUNT

        if self.state in ACTIVE_VOLCANO_STATES:
            self.volcano_fee = self.base_premium * NEAR_VOLCANO_FEE

        if self.owns_property:
            self.ownership_discount = self.base_premium * OWNERSHIP_DISCOUNT

        super(Quote, self).save(*args, **kwargs)



