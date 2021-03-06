# -*- coding: utf-8 -*-
from openerp.osv import fields,osv
from openerp import tools

class purchase_report(osv.osv):
    _inherit = "purchase.report"
    _columns = {
        'order_id': fields.many2one('purchase.order','Purchase Order'),
        'od_pdt_group_id': fields.many2one('od.product.group','Group'),
        'od_pdt_sub_group_id':fields.many2one('od.product.sub.group','Sub Group'),
        'od_pdt_classification_id':fields.many2one('od.product.classification','Classification'),
        'od_pdt_brand_id': fields.many2one('od.product.brand','Brand'),

        'od_amount_in_local_currency': fields.float('Local Currency'),
        'currency_id':fields.many2one('res.currency','Currency'),
        'od_order_type_id':fields.many2one('od.order.type','Order Type')  
#        'od_order_type_id':fields.many2one('od.order.type','Order Type'),
#        'currency_id':fields.many2one('res.currency','Currency'),
    }
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'purchase_report')
        cr.execute("""
            create or replace view purchase_report as (
                WITH currency_rate (currency_id, rate, date_start, date_end) AS (
                    SELECT r.currency_id, (1/r.rate) as rate, r.name AS date_start,
                        (SELECT name FROM res_currency_rate r2
                        WHERE r2.name > r.name AND
                            r2.currency_id = r.currency_id
                         ORDER BY r2.name ASC
                         LIMIT 1) AS date_end
                    FROM res_currency_rate r
                )
                select
                    min(l.id) as id,
                    s.date_order as date,
                    l.state,
                    l.order_id,
                    s.date_approve,
                    s.minimum_planned_date as expected_date,
         
                    s.dest_address_id,
                    s.pricelist_id,
                    s.validator,
                    spt.warehouse_id as picking_type_id,
                    s.partner_id as partner_id,
                    s.create_uid as user_id,
                    s.company_id as company_id,
                    s.od_amount_in_local_currency as od_amount_in_local_currency,
                    s.currency_id as currency_id,
                    s.od_order_type_id as od_order_type_id,
                    l.product_id,
                    t.categ_id as category_id,
                    t.uom_id as product_uom,
                    t.od_pdt_group_id,
                    t.od_pdt_sub_group_id,
                    t.od_pdt_brand_id,
                    t.od_pdt_classification_id,
                    s.location_id as location_id,
                    sum(l.product_qty/u.factor*u2.factor) as quantity,
                    extract(epoch from age(s.date_approve,s.date_order))/(24*60*60)::decimal(16,2) as delay,
                    extract(epoch from age(l.date_planned,s.date_order))/(24*60*60)::decimal(16,2) as delay_pass,
                    count(*) as nbr,
                    sum(l.price_unit*cr.rate*l.product_qty)::decimal(16,2) as price_total,
                    avg(100.0 * (l.price_unit*cr.rate*l.product_qty) / NULLIF(ip.value_float*l.product_qty/u.factor*u2.factor, 0.0))::decimal(16,2) as negociation,
                    sum(ip.value_float*l.product_qty/u.factor*u2.factor)::decimal(16,2) as price_standard,
                    (sum(l.product_qty*cr.rate*l.price_unit)/NULLIF(sum(l.product_qty/u.factor*u2.factor),0.0))::decimal(16,2) as price_average
                from purchase_order_line l
                    join purchase_order s on (l.order_id=s.id)
                        left join product_product p on (l.product_id=p.id)
                            left join product_template t on (p.product_tmpl_id=t.id)
                            LEFT JOIN ir_property ip ON (ip.name='standard_price' AND ip.res_id=CONCAT('product.template,',t.id) AND ip.company_id=s.company_id)
                    left join product_uom u on (u.id=l.product_uom)
                    left join product_uom u2 on (u2.id=t.uom_id)
                    left join stock_picking_type spt on (spt.id=s.picking_type_id)
                    join currency_rate cr on (cr.currency_id = s.currency_id and
                        cr.date_start <= coalesce(s.date_order, now()) and
                        (cr.date_end is null or cr.date_end > coalesce(s.date_order, now())))
                group by
                    s.company_id,
                    s.create_uid,
                    s.partner_id,
                    u.factor,
                    s.location_id,
                    l.price_unit,
                    s.date_approve,
                    l.date_planned,
                    l.product_uom,
                    s.minimum_planned_date,
                    s.pricelist_id,
                    s.validator,
                    s.dest_address_id,
                    l.product_id,


         
                    t.categ_id,
                    s.date_order,
                    l.state,
                    spt.warehouse_id,
                    u.uom_type,

                    t.uom_id,
                    l.order_id,
                    t.od_pdt_group_id ,
                    t.od_pdt_sub_group_id,
                    t.od_pdt_brand_id,
                    t.od_pdt_classification_id,
                    u.category_id,
                    u.id,
                    u2.factor,
                    s.od_amount_in_local_currency,
                    s.currency_id,
s.od_order_type_id
            )
        """)



#     def _select(self):
#         result = super(purchase_report, self)._select()
#         select_str = result + """,l.order_id as order_id,t.od_pdt_group_id as od_pdt_group_id,
#                               t.od_pdt_sub_group_id,t.od_pdt_classification_id
#                               """
#         return select_str
# 
# 
#     def _group_by(self):
#         result = super(purchase_report, self)._group_by()
#         group_by_str = result + """,l.order_id,t.od_pdt_group_id,
#         t.od_pdt_sub_group_id,t.od_pdt_classification_id
#                               """
#         return group_by_str
