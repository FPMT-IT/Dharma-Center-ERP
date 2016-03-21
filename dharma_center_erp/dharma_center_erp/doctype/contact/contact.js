// Copyright (c) 2016, FPMT  and contributors
// For license information, please see license.txt


frappe.ui.form.on("Contact", "validate", function(frm) {
    frm.doc.contact_name = frm.doc.prefix.trim() + " " + frm.doc.first_name.trim() + " " + frm.doc.middle_name.trim() + " " + frm.doc.last_name.trim() + " " + frm.doc.suffix.trim();
});
frappe.ui.form.on('Contact', {
	refresh: function(frm) {

	}
});
