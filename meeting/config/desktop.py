# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Meeting",
			"color": "green",
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"label": _("Meeting")
		}
	]
