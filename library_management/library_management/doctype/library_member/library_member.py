# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import dateutil
from frappe.model.document import Document
from frappe.utils import gatdate, date_diff, add_days, nowdate

class LibraryMember(Document):
	
	# This method will return full name evrytime when document is saved
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'
	
	# This method will return age from date of births
	def get_age(self):
		age_str = ""
		if self.dob:
			born = gatdate(self.dob)
			age = dateutil.relativedelta.relativedelta(gatdate(), born)
			age_str = str(age.years) + "Year(s)" + str(age.months) + "Month(s)" + str(age.days) + "Day(s(=)"
		return age_str
