# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SuscriptionDemandAmount(models.Model):
    _name = 'subscription.demand.amount'
    _inherit = 'mail.thread'
    _description = 'Demand amount'

    name = fields.Char(
        string="Name")
    amount = fields.Float(
        string="Amount")
    date = fields.Date(
        string="Date",
        tracking=True)
