import string
from django.db import models
from django.utils.crypto import get_random_string
from acme.rates import rates


def get_random_id():
    """ Generate a random 10 digit key """

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
        self.base_premium = rates.BASE_TERM_RATE

        if self.has_cancelled:
            self.cancelled_fee = self.base_premium * rates.HAS_CANCELLED_FEE
        else:
            self.not_cancelled_discount = self.base_premium * rates.NOT_CANCELLED_DISCOUNT

        if self.state in rates.ACTIVE_VOLCANO_STATES:
            self.volcano_fee = self.base_premium * rates.NEAR_VOLCANO_FEE

        if self.owns_property:
            self.ownership_discount = self.base_premium * rates.OWNERSHIP_DISCOUNT

        super(Quote, self).save(*args, **kwargs)
