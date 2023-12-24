from policyengine_us.model_api import *


class ca_fytc_eligible(Variable):
    value_type = bool
    entity = Person
    label = "FYTC Eligible"
    definition_period = YEAR
    reference = "https://www.ftb.ca.gov/forms/2022/2022-3514.pdf#page=4"

    def formula(person, period, parameters):
        p = parameters(period).gov.states.ca.tax.income.credits.foster_youth

        age = person("age", period)

        meets_age_requirements = (
            (age >= p.min_age)
            & (age <= p.max_age)
        )

        eitc_eligibility = person.tax_unit(
            "ca_eitc_eligible", period
        )

        in_foster_care = person("ca_foster_care", period)

        head_or_spouse = person("is_tax_unit_head_or_spouse", period)

        return meets_age_requirements & eitc_eligibility & in_foster_care & head_or_spouse

#TODO: create a ca_foster_care.py -> empty bool | person level 