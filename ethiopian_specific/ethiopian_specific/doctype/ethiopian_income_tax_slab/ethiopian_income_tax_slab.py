# Copyright (c) 2024, mevinai and contributors
# For license information, please see license.txt

from frappe.model.document import Document

# import frappe
import erpnext


class EthiopianIncomeTaxSlab(Document):
	def validate(self):
		if self.company:
			self.currency = erpnext.get_company_currency(self.company)
