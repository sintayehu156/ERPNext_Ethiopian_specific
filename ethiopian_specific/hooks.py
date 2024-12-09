app_name = "ethiopian_specific"
app_title = "Ethiopian Specific"
app_publisher = "mevinai"
app_description = "Ethiopian Specific ERPNext functionalities"
app_email = "info@mevinai.com"
app_license = "mit"

import hrms.payroll.doctype.salary_slip.salary_slip
from ethiopian_specific.overrides.salary_slip import custom_calculate_tax_by_tax_slab
# from ethiopian_specific.overrides.salary_slip import custom_calculate_variable_tax
# from ethiopian_specific.overrides.salary_slip import custom_compute_income_tax_breakup

hrms.payroll.doctype.salary_slip.salary_slip.calculate_tax_by_tax_slab = custom_calculate_tax_by_tax_slab
# hrms.payroll.doctype.salary_slip.salary_slip.calculate_variable_tax = custom_calculate_variable_tax
# hrms.payroll.doctype.salary_slip.salary_slip.compute_income_tax_breakup = custom_compute_income_tax_breakup

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ethiopian_specific",
# 		"logo": "/assets/ethiopian_specific/logo.png",
# 		"title": "Ethiopian Specific",
# 		"route": "/ethiopian_specific",
# 		"has_permission": "ethiopian_specific.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ethiopian_specific/css/ethiopian_specific.css"
# app_include_js = "/assets/ethiopian_specific/js/ethiopian_specific.js"

# include js, css files in header of web template
# web_include_css = "/assets/ethiopian_specific/css/ethiopian_specific.css"
# web_include_js = "/assets/ethiopian_specific/js/ethiopian_specific.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ethiopian_specific/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ethiopian_specific/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ethiopian_specific.utils.jinja_methods",
# 	"filters": "ethiopian_specific.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ethiopian_specific.install.before_install"
# after_install = "ethiopian_specific.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ethiopian_specific.uninstall.before_uninstall"
# after_uninstall = "ethiopian_specific.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ethiopian_specific.utils.before_app_install"
# after_app_install = "ethiopian_specific.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ethiopian_specific.utils.before_app_uninstall"
# after_app_uninstall = "ethiopian_specific.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ethiopian_specific.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ethiopian_specific.tasks.all"
# 	],
# 	"daily": [
# 		"ethiopian_specific.tasks.daily"
# 	],
# 	"hourly": [
# 		"ethiopian_specific.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ethiopian_specific.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ethiopian_specific.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ethiopian_specific.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ethiopian_specific.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ethiopian_specific.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ethiopian_specific.utils.before_request"]
# after_request = ["ethiopian_specific.utils.after_request"]

# Job Events
# ----------
# before_job = ["ethiopian_specific.utils.before_job"]
# after_job = ["ethiopian_specific.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ethiopian_specific.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

