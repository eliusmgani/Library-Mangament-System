# -*- coding: utf-8 -*-
# Copyright (c) 2021, lee22jar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            # Set the Article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.status = "Issued"
            article.save()

        elif self.type == "Return":
            self.validate_return()
            # Set the Article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.status = "Available"
            article.save()

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # Article cannot be Issued if it is already Issued
        if article.status == "Issued":
            frappe.throw("Article is already Issued by another Member")

    def validate_return(self):
        # self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # Artcile cannot be Returned if is not Issued first
        if article.status == "Availabe":
            frappe.throw(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                "Article cannot be Returned without being Issued first")

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value(
            "Library Setting", "maximum_number")
        count = frappe.db.count(
            "Library Transaction",
            {
                "library_member": self.library_member,
                "type": "Issue",
                "docstatus": 1
            },
        )
        if count >= max_articles:
            frappe.throw("Maximum Limit reached for Issuing Articles")

    def validate_membership(self):
        # Check if a Valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "from_date": ("<", self.date),
                "to_date": (">", self.date)
            }
        )
        if not valid_membership:
            frappe.throw("The Member does not have a valid Membership")
