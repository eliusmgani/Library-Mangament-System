// Copyright (c) 2021, lee22jar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member', {
	refresh: function(frm) {
		frm.add_custom_button("Create MemberShip", () => {
			frappe.new_doc("Library Membership", {
				"library_membership": frm.doc.name
			})
		})
		frm.add_custom_button("Create Transaction", () => {
			frappe.new_doc("Library Transaction", {
				"library_trnsaction": frm.doc.name
			})
		})

	}
	
});
frappe.ui.form.on("Library Member", 'dob', function(frm){
	if(frm.doc.dob){
		let today  = new Date();
		let birthDate = new Date(frm.doc.dob);
		if(today < birthDate){
			frappe.msgprint(__("Please Select a Valid Date"));
			frappe.model.set_value(frm.doctype, frm.docname, dob, '');
		}
		else{
			let age_str = get_age(frm.doc.dob);
			$(frm.fields_dict['age_html'].wrapper).html('AGE: ' + age_str);
		}
	}
	else{
		$(frm.fields_dict['age_html'].wrapper).html();
	}
});

let get_age = function(birth){
	let ageMS = Date.parse(Date()) - Date.parse(birth);
	let age = new Date();
	age.setTime(ageMS);
	let years = age.getFullYear() - 1970;
	return years + ' Year(s) ' + age.getMonth() + ' Month(s) ' +  age.getDate() + ' Day(s)';
}

/*
frappe.ui.form.on('Library Member', 'date_of_birth', function(frm){
	cur_frm.set_value(age, moment().diff(cur_frm.doc.date_of_birth, 'years'));
	cur_frm.refresh_field(age);
});
*/