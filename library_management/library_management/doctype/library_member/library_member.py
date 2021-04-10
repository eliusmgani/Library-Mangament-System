# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    # Thismethod will return full name every time when the document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
"""
    def get_age(self):
        age_str = ""
        if self.date_of_birth:
            born = getdate(self.date_of_birth)
            age = dateutil.relativedelta.relativedelta(getdate(), born)
            age_str = str(age.years) + " year(s) " + str(age.months) + " month(s) " + str(age.days) + " day(s) "
            return age_str
"""