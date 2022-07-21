# Acme Insurance Rates

BASE_TERM_RATE = 59.94
TERM_LENGTH_IN_MONTHS = 6

ACTIVE_VOLCANO_STATES = {'AK',  # Alaska
                         'AZ',  # Arizona
                         'CA',  # California
                         'CO',  # Colorado
                         'HI',  # Hawaii
                         'ID',  # Idaho
                         'NV',  # Nevada
                         'NM',  # New Mexico
                         'OR',  # Oregon
                         'UT',  # Utah
                         'WA',  # Washington
                         'WY'}  # Wyoming

# FEES
HAS_CANCELLED_FEE = 0.15 * BASE_TERM_RATE
NEAR_VOLCANO_FEE = 0.25 * BASE_TERM_RATE

# DISCOUNTS
NOT_CANCELLED_DISCOUNT = -0.10 * BASE_TERM_RATE
OWNERSHIP_DISCOUNT = -0.20 * BASE_TERM_RATE
