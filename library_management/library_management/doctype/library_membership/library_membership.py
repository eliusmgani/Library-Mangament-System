# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	# Check before submitting this docment
	def before_submit(self):
		exists = frappe.db.exists("Library Membership", 
            {
				"library_member": self.library_member,
				#check for submitted documents
				"docstatus": 1,
				# check if the membership's end date is later than the this membership's start date
				"to_date": (">", self.from_date),
			},
        )
		if exists:
			frappe.throw("There is an active Membership for this member")
		# Get loan period and compute to_date by adding loan_period to from_date
		loan_period = frappe.db.get_single_value("Library Setting", "loan_period")
		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)