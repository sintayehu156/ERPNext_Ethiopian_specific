
import frappe

# def execute():
#     if not frappe.db.exists("Custom Field", {"dt": "Ethiopian Taxable Salary Slab", "fieldname": "deductible_fee"}):
#         custom_field = frappe.get_doc({
#             "doctype": "Custom Field",            
#             "dt": "Ethiopian Taxable Salary Slab", 
#             "fieldname": "deductible_fee", 
#             "fieldtype": "Currency",  
#             "label": "Deductible Fee",
#             "insert_after": "percent_deduction",  
#             "in_list_view": 1,  
#         }).insert()
        
#         # Commit the transaction to ensure changes are saved to the database
#         frappe.db.commit()
        
#         # Fetch the newly added field data for verification and print it
#         added_field = frappe.get_doc("Custom Field", custom_field.name)
#         print("Custom Field Added:", added_field.as_dict())
#     else:
#         print("The field 'deductible_fee' already exists in the 'Ethiopian Taxable Salary Slab' child table.")


import frappe

def execute():
    try:
        # Check if the field already exists
        if not frappe.db.exists("Custom Field", {"dt": "Ethiopian Taxable Salary Slab", "fieldname": "deductible_fee"}):
            # Log the action of creating a new custom field
            print("Creating 'deductible_fee' field in 'Ethiopian Taxable Salary Slab'...")
            
            # Create the custom field document
            custom_field = frappe.get_doc({
                "doctype": "Custom Field",
                "dt": "Ethiopian Taxable Salary Slab",
                "fieldname": "deductible_fee",
                "fieldtype": "Currency",
                "label": "Deductible Fee",
                "insert_after": "percent_deduction",
                "in_list_view": 1,
            })
            
            # Insert the document and commit the transaction
            custom_field.insert()
            frappe.db.commit()

            # Fetch the newly added field for verification
            added_field = frappe.get_doc("Custom Field", custom_field.name)
            print("Custom Field Added:", added_field.as_dict())
        else:
            print("The field 'deductible_fee' already exists in the 'Ethiopian Taxable Salary Slab' child table.")
    
    except frappe.ValidationError as e:
        print("Validation error occurred:", e)
    except frappe.DoesNotExistError as e:
        print("Document does not exist error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
