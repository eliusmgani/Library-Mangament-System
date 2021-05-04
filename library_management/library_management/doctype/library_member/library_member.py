# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_years, nowdate, date_diff


class LibraryMember(Document):
    # Thismethod will return full name every time when the document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

    def get_age(self):
        age = ""
        if self.date_of_birth:
            born = getdate(self.date_of_birth)
            age = dateutil.relativedelta.relativedelta(gatdate(), born)
            age_str = str(age.years) + ' Year(s) ' + str(age.months) + ' Month(s) ' + str(age.days) + ' Day(s) '
        return age


# date_diff(nowdate(), add_years(getdate(self.date_of_birth), student_admission.min_age)) < 0:
# 

