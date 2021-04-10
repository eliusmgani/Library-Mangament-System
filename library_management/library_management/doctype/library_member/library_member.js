// Copyright (c) 2021, lee22jar and contributors
// For license information, please see license.txt
/*
frappe.ui.form.on('Library Member', {
	refresh: function(frm) {

	},
	onload: function (frm) {
		if(frm.doc.date_of_birth){
			$(frm.fields_dict['age_html'].wrapper).html("AGE : " + get_age(frm.doc.date_of_birth));
		}
	}
});

frappe.ui.form.on('Library Member', 'date_of_birth', function(frm) {
	if(frm.doc.date_of_birth){
		var today = new Date();
		var birthDate = new Date(frm.doc.date_of_birth);
		var age_str = get_age(frm.doc.date_of_birth);
		$(frm.fields_dict['age_html'].wrapper).html("AGE : " + age_str);
	}
});

var get_age = function (birth) {
	var ageMS = Date.parse(Date()) - Date.parse(birth);
	var age = new Date();
	age.setTime(ageMS);
	var years = age.getFullYear() - 1970;
	return years + " Year(s) " + age.getMonth() + " Month(s) " + age.getDate() + " Day(s) ";
};
*/


frappe.ui.form.on('Library Member', 'date_of_birth', function(frm){
	cur_frm.set_value(age, moment().diff(cur_frm.doc.date_of_birth, 'years'));
	cur_frm.refresh_field(age);
});

/*

cur_frm.set_value(AgeField, moment().diff(cur_frm.doc.DATEFIELDNAME, 'years'));
cur_frm.refresh_field(AgeField)

*/

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