# -*- coding: utf-8 -*-
{
    "name" : "Orchid Stock Reports",
    "version" : "0.1",
    "author": "OrchidERP",
    "category" : "Warehouse Management",
    "description": """OrchidERP Stock Reports""",
    "website": ["http://www.orchiderp.com"],
    "depends": ['stock','product_expiry','orchid_report','orchid_product'],
    "data" : [
			'security/orchid_stock_security.xml',
            'security/ir.model.access.csv',
			'wizard/stock_transfer_details.xml',
            'wizard/od_stock_aging_report_view.xml',
            'wizard/od_closing_inventory_wiz_view.xml',
            'wizard/stock_move_wiz_view.xml',
            'wizard/stock_move_wiz_qty_view.xml',
            'wizard/location_stock_wiz_view.xml',
            'stock/stock_view.xml',
            'views/report_stock_aging.xml',
            'views/report_stock_list.xml',
            'views/report_stock_aging_detail.xml',
            'views/report_stock_closing.xml',
            'views/report_stock_move_analysis.xml',
            'views/quant_view.xml',
#             'stocklist/stocklist_view.xml',
            'report/od_stock_history_view.xml',
            'report/od_stock_history_qty_view.xml',
            'wizard/od_quant_wiz_view.xml',
            'wizard/od_stock_quant_view.xml',
            'report.xml',
            'report/od_location_stock.xml',
            'report/od_quant_move_analysis_view.xml',
            'report/od_stock_move_analysis_view.xml',
            'report/od_stock_move_quantity_analysis_view.xml',
            'report/od_stock_empty_location_report_view.xml',

            'report_menu.xml',

            ],
    'css': [],
}
