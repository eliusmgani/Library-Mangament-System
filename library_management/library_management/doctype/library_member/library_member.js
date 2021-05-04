// Copyright (c) 2021, lee22jar and contributors
// For license information, please see license.txt



frappe.ui.form.on("Library Member", {
	refresh: function(frm){
		frm.add_custom_button("Create Membership", () => {
			frappe.new_doc("Library Membership", {
				'library_membership': frm.doc.name
			})
		})
		frm.add_custom_button("Create Transaction", () => {
			frappe.new_doc("Library Transaction", {
				'library_transaction': frm.doc.name
			})
		})
	}
});

frappe.ui.form.on('Library Member', 'date_of_birth', function(frm){
	if (frm.doc.date_of_birth){
		let today = new Date();
		let birthDate = new Date(frm.doc.date_of_birth);
		if(today < birthDate){
			frappe._msgprint(_("Please Select a Valid Date"));
			frappe.model.set_value(frm.doctype, frm.docname, date_of_birth, '');
		}
		else{
			let age = get_age(frm.doc.date_of_birth);
			$(frm.fields_dict['age_html'].wrapper).html('AGE: ' + age);
		}
	}
	else{
		$(frm.fields_dict['age_html'].wrapper).html();
	}
});

let get_age = function(birth){
	let ageMS = Date.parse(Date()) - Date.parse(birth);
	let age_ = new Date();
	age.setTime(ageMs);
	let years = age_.getFullYear() - 1970;
	return years + ' Year(s) ' + age_.getMonth() + ' Month(s)' + age_.getDate() + 'Day(s)';
};
/*
frappe.ui.form.on('Library Member', 'date_of_birth', function(frm){
	cur_frm.set_value(age, moment().diff(cur_frm.doc.date_of_birth, 'years'));
	cur_frm.refresh_field(age);
});
*/