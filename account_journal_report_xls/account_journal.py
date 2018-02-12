# -*- encoding: utf-8 -*-
##############################################################################

from openerp.osv import orm
from openerp.addons.report_xls.utils import rowcol_to_cell, _render
from openerp.tools.translate import _


class account_journal(orm.Model):
    _inherit = 'account.journal'

    # allow inherited modules to extend the query
    def _report_xls_query_extra(self, cr, uid, context=None):
        select_extra = ""
        join_extra = ""
        where_extra = ""
        return (select_extra, join_extra, where_extra)

    # allow inherited modules to add document references
    def _report_xls_document_extra(self, cr, uid, context=None):
        return "''"

    # allow inherited modules to extend the render namespace
    def _report_xls_render_space_extra(self, cr, uid, context=None):
        """
        extend render namespace for use in the template 'lines', e.g.
        space_extra = {
            'partner_obj': self.pool.get('res.partner'),
        }
        return space_extra
        """
        return None

    # override list in inherited module to add/drop columns or change order
    def _report_xls_fields(self, cr, uid, context=None):
        res = [
            'move_name',         # account.move,name
            'move_date',         # account.move,date
            'acc_code',          # account.account,code
        ]
        if context.get('print_by') == 'fiscalyear':
            res += [
                'period',        # account.period,code or name
            ]
        res += [
            'partner_name',      # res.partner,name
            'aml_name',          # account.move.line,name
            'tax_code',          # account.tax.code,code
            'tax_amount',        # account.move.line,tax_amount
            'debit',             # account.move.line,debit
            'credit',            # account.move.line,credit
            'balance',           # debit-credit
            'docname',           # origin document if any
            #'date_maturity',     # account.move.line,date_maturity
            #'reconcile',         # account.move.line,reconcile_id.name
            #'reconcile_partial', # account.move.line,reconcile_partial_id.name
            #'partner_ref',       # res.partner,ref
            #'move_ref',          # account.move,ref
            #'move_id',           # account.move,id
            #'acc_name',          # account.account,name
            #'journal',           # account.journal,name
            #'journal_code',      # account.journal,code
            #'analytic_account',       # account.analytic.account,name
            #'analytic_account_code',  # account.analytic.account,code
        ]
        return res

    # Change/Add Template entries
    def _report_xls_template(self, cr, uid, context=None):
        """
        Template updates, e.g.

        my_change = {
            'move_name':{
                'header': [1, 20, 'text', _render("_('My Move Title')")],
                'lines': [1, 0, 'text', _render("l['move_name'] != '/' and l['move_name'] or ('*'+str(l['move_id']))")],
                'totals': [1, 0, 'text', None]},
        }
        return my_change
        """
        return {}
