from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    paidtate_ids = fields.One2many(
        comodel_name='bim.paidstate',
        inverse_name='invoice_id',
        string='Estados de Pago'
    )
    paidstate_by_bim_project_ids = fields.Many2many(
        comodel_name='bim.paidstate',
        compute='_compute_paidstate_by_bim_project_ids',
        string='Estado de Pago por Obra',
    )

    @api.depends('paidtate_ids')
    def _compute_paidstate_by_bim_project_ids(self):
        for move in self:
            move.paidstate_by_bim_project_ids = move.paidtate_ids.filtered(
                lambda x: x.project_id == move.project_id
                and x.state == 'invoiced'
            )
