app_name = "whatsapp_integration"
app_title = "Whatsapp Chat"
app_publisher = "shridhar patil"
app_description = "Chat app for whatsapp"
app_email = "shridharpatil2792@gmail.com"
app_license = "unlicense"
# required_apps = []

# Includes in <head>
# ------------------
from frappe import __version__ as frappe_version

is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13

app_include_css = ['whatsapp_integration.bundle.css'] if is_frappe_above_v13 else [
    '/assets/css/whatsapp_integration.css']

app_include_js = ['whatsapp_integration.bundle.js'] if is_frappe_above_v13 else [
    '/assets/js/whatsapp_integration.js']

# include js, css files in header of desk.html
# app_include_css = "/assets/whatsapp_integration/css/whatsapp_integration.css"
# app_include_js = "/assets/whatsapp_integration/js/whatsapp_integration.bundle.js"

# include js, css files in header of web template
# web_include_css = "/assets/whatsapp_integration/css/whatsapp_integration.css"
# web_include_js = "/assets/whatsapp_integration/js/whatsapp_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "whatsapp_integration/public/scss/website"

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
# app_include_icons = "whatsapp_integration/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "whatsapp_integration.utils.jinja_methods",
#	"filters": "whatsapp_integration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "whatsapp_integration.install.before_install"
# after_install = "whatsapp_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "whatsapp_integration.uninstall.before_uninstall"
# after_uninstall = "whatsapp_integration.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "whatsapp_integration.utils.before_app_install"
# after_app_install = "whatsapp_integration.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "whatsapp_integration.utils.before_app_uninstall"
# after_app_uninstall = "whatsapp_integration.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "whatsapp_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
    "WhatsApp Message": {
        "after_insert":"whatsapp_integration.api.message.last_message"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"whatsapp_integration.tasks.all"
#	],
#	"daily": [
#		"whatsapp_integration.tasks.daily"
#	],
#	"hourly": [
#		"whatsapp_integration.tasks.hourly"
#	],
#	"weekly": [
#		"whatsapp_integration.tasks.weekly"
#	],
#	"monthly": [
#		"whatsapp_integration.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "whatsapp_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "whatsapp_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "whatsapp_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["whatsapp_integration.utils.before_request"]
# after_request = ["whatsapp_integration.utils.after_request"]

# Job Events
# ----------
# before_job = ["whatsapp_integration.utils.before_job"]
# after_job = ["whatsapp_integration.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"whatsapp_integration.auth.validate"
# ]

sounds = [
    {'name': 'chat-notification', 'src': '/assets/frappe/sounds/email.mp3', 'volume': 0.2},
    {'name': 'chat-message-send', 'src': '/assets/frappe/sounds/submit.mp3', 'volume': 0.2},
    {'name': 'chat-message-receive', 'src': '/assets/frappe/sounds/alert.mp3', 'volume': 0.5}
]