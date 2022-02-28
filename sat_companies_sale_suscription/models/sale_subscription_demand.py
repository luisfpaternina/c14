# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleSuscriptionDemand(models.Model):
    _name = 'sale.subscription.demand'
    _inherit = 'mail.thread'
    _description = 'Demands'
    _rec_name = 'code'

    name = fields.Char(string="Name")
    code = fields.Char(string="Demand number")
    date = fields.Date(string="Date")
