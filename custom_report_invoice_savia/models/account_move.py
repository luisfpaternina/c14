from odoo import api, fields, models, _


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
    bim_masive_certification_ids = fields.Many2many(
        comodel_name='bim.masive.certification.by.line',
        'account_move_bim_massive_certification_by_line_rel',
        string='Certificación masiva',
    )
    bim_masive_chapter_ids = fields.Many2many(
        comodel_name='bim.massive.chapter.certification',
        'account_move_bim_massive_chapter_rel',
        string='Certificación capítulo',
    )

    @api.depends('paidtate_ids')
    def _compute_paidstate_by_bim_project_ids(self):
        for move in self:
            move.paidstate_by_bim_project_ids = move.paidtate_ids.filtered(
                lambda x: x.project_id == move.project_id
                and x.state == 'invoiced'
            )
