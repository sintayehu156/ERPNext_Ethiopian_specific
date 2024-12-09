from hrms.payroll.doctype.salary_slip.salary_slip import calculate_tax_by_tax_slab
from hrms.payroll.doctype.salary_slip.salary_slip import SalarySlip
from hrms.payroll.doctype.payroll_period.payroll_period import (
	get_payroll_period
    )
from datetime import datetime
import frappe
from frappe.utils import (
	flt
)

def custom_calculate_tax_by_tax_slab(start_date, end_date, company, annual_taxable_earning, tax_slab, earnings, eval_globals=None, eval_locals=None):
    percent = 0
    tax_amount = 0
    deductable_fee = 0
    
    for component in earnings:
        if component.is_flexible_benefit and component.is_tax_applicable:
            annual_taxable_earning += (component.amount*12)

    for slab in tax_slab.slabs:
        if (annual_taxable_earning >= slab.from_amount and annual_taxable_earning < slab.to_amount) or (not slab.to_amount and annual_taxable_earning >= slab.from_amount):
            percent = slab.percent_deduction * 0.01
            if slab.deductible_fee:
                deductable_fee = slab.deductible_fee
            break
    
    def calculate_month_difference(start_date, end_date):
        # If the dates are not already in string format, assume they are date objects and skip conversion
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Extract year and month from both dates
        start_year = start_date.year
        start_month = start_date.month
        end_year = end_date.year
        end_month = end_date.month

        # Calculate the difference in months considering the year and month
        month_difference = (end_year - start_year) * 12 + (end_month - start_month)

        return month_difference
        
    payroll_period = get_payroll_period(start_date, end_date, company)
    month_difference = calculate_month_difference(payroll_period.start_date, start_date)
    annual_taxable_earning += month_difference * 0.0
    
    tax_amount = annual_taxable_earning * percent

    return tax_amount, deductable_fee


def custom_calculate_variable_tax(self, tax_component):
		self.previous_total_paid_taxes = self.get_tax_paid_in_period(
			self.payroll_period.start_date, self.start_date, tax_component
		)

		# Structured tax amount
		eval_locals, default_data = self.get_data_for_eval()
		tax_amount, deductable_fee = calculate_tax_by_tax_slab(
		self.start_date,
		self.end_date,
		self.company,
		self.total_taxable_earnings_without_full_tax_addl_components,
		self.tax_slab,
		self.earnings,
		self.whitelisted_globals,
		eval_locals,
		)


		self.total_structured_tax_amount = tax_amount
		self.current_structured_tax_amount = (
		self.total_structured_tax_amount
		) / 12
		self.current_structured_tax_amount -= deductable_fee

	
		
		self.full_tax_on_additional_earnings = 0.0
		if self.current_additional_earnings_with_full_tax:
			self.total_tax_amount = calculate_tax_by_tax_slab(
				self.start_date, self.end_date, self.company, self.total_taxable_earnings, self.tax_slab, self.earnings, self.whitelisted_globals, eval_locals
			)
			self.full_tax_on_additional_earnings = self.total_tax_amount - self.total_structured_tax_amount

		current_tax_amount = self.current_structured_tax_amount + self.full_tax_on_additional_earnings
		if flt(current_tax_amount) < 0:
			current_tax_amount = 0

		self._component_based_variable_tax[tax_component].update(
			{
				"previous_total_paid_taxes": self.previous_total_paid_taxes,
				"total_structured_tax_amount": self.total_structured_tax_amount,
				"current_structured_tax_amount": self.current_structured_tax_amount,
				"full_tax_on_additional_earnings": self.full_tax_on_additional_earnings,
				"current_tax_amount": current_tax_amount,
			}
		)

		return current_tax_amount

def custom_compute_income_tax_breakup(self):
		if not self.payroll_period:
			return

		self.standard_tax_exemption_amount = 0
		self.tax_exemption_declaration = 0
		self.deductions_before_tax_calculation = 0

		self.non_taxable_earnings = self.compute_non_taxable_earnings()

		self.ctc = self.compute_ctc()

		self.income_from_other_sources = self.get_income_form_other_sources()

		self.total_earnings = self.ctc + self.income_from_other_sources

		if hasattr(self, "tax_slab"):
			if self.tax_slab.allow_tax_exemption:
				self.standard_tax_exemption_amount = self.tax_slab.standard_tax_exemption_amount
				self.deductions_before_tax_calculation = (
					self.compute_annual_deductions_before_tax_calculation()
				)

			self.tax_exemption_declaration = (
				self.get_total_exemption_amount() - self.standard_tax_exemption_amount
			)

		self.annual_taxable_amount = self.total_earnings - (
			self.non_taxable_earnings
			+ self.deductions_before_tax_calculation
			+ self.tax_exemption_declaration
			+ self.standard_tax_exemption_amount
		)

		self.income_tax_deducted_till_date = self.get_income_tax_deducted_till_date()

		if hasattr(self, "total_structured_tax_amount") and hasattr(self, "current_structured_tax_amount"):
			self.future_income_tax_deductions = (
				# self.total_structured_tax_amount - self.income_tax_deducted_till_date
				self.total_structured_tax_amount 
			)

			self.current_month_income_tax = self.current_structured_tax_amount

			# non included current_month_income_tax separately as its already considered
			# while calculating income_tax_deducted_till_date

			# self.total_income_tax = self.income_tax_deducted_till_date + self.future_income_tax_deductions
			self.total_income_tax = self.future_income_tax_deductions
