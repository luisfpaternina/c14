# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import logging


class AccountMove(models.Model):
    _inherit = 'account.move'

    product_id = fields.Many2one(
        'product.template',
        'Gadgets',
        compute="_compute_gadget_name")
    gadgets_contract_type_id = fields.Many2one(
        'stock.gadgets.contract.type')
    task_user_id = fields.Many2one(
        'res.users',
        compute="_compute_gadget_name")
    sale_type_id = fields.Many2one(
        'sale.order.type')
    date_begin = fields.Datetime(
        string = 'Date asigned')
    date_end = fields.Datetime(
        string = 'Date End asingned')
    gadget_contract_type = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Contract type")
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True,
        related="partner_id.is_potential_client")
    check_product = fields.Boolean(
        compute='compute_check_product')
    check_contract_type = fields.Boolean(
        compute="_compute_check_contract_type")
    rae = fields.Char(
        string="R.A.E",
        related="product_id.rae")
    subscription_template_id = fields.Many2one(
        'sale.subscription.template',
        string="Subscription template",
        related="product_id.subscription_template_id")
    subscription_id = fields.Many2one(
        'sale.subscription',
        string="Subscription",
        compute="_compute_subscription")


    @api.depends('partner_id')
    def _compute_subscription(self):
        for line in self.invoice_line_ids:
            if line.subscription_id:
                self.subscription_id = line.subscription_id.id
            else:
                self.subscription_id = False

    @api.depends('subscription_id')
    def _compute_gadget_name(self):
        for record in self:
            if record.subscription_id:
                record.product_id = record.subscription_id.product_id.id
                record.task_user_id = record.subscription_id.task_user_id.id
            else:
                record.product_id = False
                record.task_user_id = False


    @api.depends('sale_type_id')
    def _compute_check_contract_type(self):
        for record in self:
            if record.sale_type_id.code == '01':
                record.check_contract_type = True
            else:
                record.check_contract_type = False

    @api.depends('product_id')
    def compute_check_product(self):
        for record in self:
            if record.product_id:
                record.check_product=True
            else:
                record.check_product=False

    @api.onchange('product_id')
    def onchange_check_product(self):
        for record in self:
            if record.product_id.employee_notice_id.user_id:
                record.task_user_id = record.product_id.employee_notice_id.user_id
            sale_type = record.product_id.subscription_template_id.sale_type_id
            gadgets_contract = record.product_id.subscription_template_id.gadgets_contract_type_id
            record.sale_type_id = sale_type
            record.gadgets_contract_type_id = gadgets_contract