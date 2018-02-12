# -*- coding: utf-8 -*-
{

	'name': 'Orchid Beta Project',
	'version': '1.0',
	'category': 'Production',
	'summary': 'Orchid Beta Project',
	'author': 'OrchidERP',
	'website': 'https://orchiderp.com',
	'depends': ['base','project','project_issue','hr','orchid_product','mail','analytic','hr_expense','orchid_cost_centre','orchid_cost_sheet'],
	'data': [
			'security/ir.model.access.csv',
			'data/mail_template.xml',
			'data/contract_expiry_sch.xml',
			'wizard/confirm_wiz_view.xml',
            'views/project_open_kanban_view.xml',
            'project_view_minimal.xml',
			'project_view.xml',
			'od_sub_category.xml',
			'od_implementation.xml',
			'od_project_status.xml',
			'purchase/purchase_view.xml',
			'menus/technical.xml',
			'stock/stock_view.xml',
# 			'views/od_project_changes.xml',
			'wizard/gen_purchase_view.xml',
			'wizard/gen_stock_picking_view.xml',
			'wizard/wiz_assign_user_view.xml',
			'data/data.xml',
            'analytic_view.xml',
            'views/pack_op_lot.xml',
            'timesheet/hr_contract_view.xml',
            'timesheet/timesheet_view.xml',
            'hr_expense/hr_expense_view.xml',
            'crm/crm_view.xml',
            'views/project_task_work.xml',
            'crm/account_move_line_view.xml',
            'helpdesk/scheduler.xml',
            'helpdesk/seq.xml',
            'helpdesk/crm_helpdesk_view.xml',
			],
	'demo': [],
	'test': [],
	'installable': True,
	'auto_install': False,
	'application': True,

}
