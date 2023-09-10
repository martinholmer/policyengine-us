from policyengine_us.model_api import *


class co_ctc_eligible_children_count(Variable):
    value_type = int
    entity = Person
    label = "Colorado child tax credit eligible children count"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://leg.colorado.gov/sites/default/files/2023a_1112_signed.pdf#page=2",
    )
    defined_for = StateCode.CO

    adds = ["co_ctc_eligible_child"]
