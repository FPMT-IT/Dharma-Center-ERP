# -*- coding: utf-8 -*-
# Copyright (c) 2015, FPMT  and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Contact(Document):
	pass
#	def validate(self):
#		self.contact_name = compose_contact_name(self) 
    
#@frappe.whitelist()    
#def compose_contact_name(Contact):
#    """Compose contact_name with prefix + first name + middle name + last name + suffix"""
#    print("here!!")
#    return " ".join(filter(Contact.prefix.strip(), " ", Contact.first_name.strip(), " ", Contact.middle_name.strip(), " ", Contact.last_name.strip(), " ", Contact.suffix.strip()))
      
    
