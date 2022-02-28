# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleSuscriptionDemand(models.Model):
    _name = 'sale.subscription.demand'
    _inherit = 'mail.thread'
    _description = 'Demands'
    _rec_name = 'code'

    name = fields.Char(
        string="Name",
        tracking=True)
    code = fields.Char(
        string="Demand number",
        tracking=True)
    date = fields.Date(
        string="Date",
        tracking=True)
    partner_id = fields.Many2one(
        'res.partner',
        string="Partner",
        tracking=True)
    street = fields.Char(
        related="partner_id.street",
        string="Address")
    phone = fields.Char(
        related="partner_id.mobile",
        string="Phone")
    email = fields.Char(
        string="Email",
        related="partner_id.email")
    state_id = fields.Many2one(
        'res.country.state',
        string="State",
        related="partner_id.state_id")
    city = fields.Char(
        string="Population",
        related="partner_id.city")
    is_embargo = fields.Boolean(
        string="Embargo",
        tracking=True)
    observations = fields.Text(
        string="Observations",
        tracking=True)
    notes = fields.Text(
        string="Notes",
        tracking=True)
    demand_line_ids = fields.One2many(
        'subscription.demand.amount',
        'demand_id',
        string="Amounts")
    subscription_type_id = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Subscription type",
        tracking=True)
    reason_change_id = fields.Many2one(
        'subscription.reason.change',
        string="Reason change",
        tracking=True)
