from policyengine_us.model_api import *


class ca_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "CA AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.ftb.ca.gov/forms/2021/2021-540.pdf"
        "https://www.ftb.ca.gov/forms/2022/2022-540.pdf"
    )
    defined_for = StateCode.CA

    def formula(tax_unit, period, parameters):
        federal_agi = tax_unit("adjusted_gross_income", period)
        subtractions = tax_unit("ca_agi_subtractions", period)
        additions = tax_unit("ca_agi_additions", period)
        return max_(0, federal_agi - subtractions) + additions
