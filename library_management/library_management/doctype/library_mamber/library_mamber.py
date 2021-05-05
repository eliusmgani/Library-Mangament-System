# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_years, nowdate, date_diff

class LibraryMamber(Document):
	
	# This method will return full name everytime when the document is saved.
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'
	
	# This method will return Age from date of birth
	def get_age(self):
		age = ""
		if self.dob:
			born = getdate(self.dob)
			age = deltautils.relativedelta.relativedelta(getdt(), born)
			age_str = str(age.years) + " Year(s) " + str(age.months) + " Month(s) " + str(ge.days) + "Days"
		return age_str