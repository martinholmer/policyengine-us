from policyengine_us.model_api import *


class ca_amti(Variable):
    value_type = float
    entity = TaxUnit
    label = "CA alternative minimum taxable income"
    defined_for = StateCode.CA
    unit = USD
    definition_period = YEAR
    reference = ""

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        p = parameters(period).gov.states.ca.tax.income.alternative_minimum_tax
        
        total_adjustments = tax_unit("total_adjustments", period) # line 14 Total Adjustments and Preferences
        taxable_income = tax_unit("ca_taxable_income", period) # line 15 taxable income
        # line 16 Net operating loss (NOL) 
        # line 17 AMTI exclusion from trade or business income
        itemized_ded_limitation = tax_unit("itemized_ded_limitation", period) # line 18
        amti_before_ded = total_adjustments + taxable_income + itemized_ded_limitation # line 19
        # line 20 Alternative minimum tax NOL deduction

        return amti_before_ded
            
        
        