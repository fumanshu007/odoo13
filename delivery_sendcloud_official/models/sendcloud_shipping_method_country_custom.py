# Copyright 2021 Onestein (<https://www.onestein.eu>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class SendCloudShippingMethodCountryCustom(models.Model):
    _name = "sendcloud.shipping.method.country.custom"
    _description = "SendCloud Shipping Method Country Custom"

    iso_2 = fields.Char(required=True)
    price = fields.Float()
    method_code = fields.Integer(required=True)
    company_id = fields.Many2one("res.company", required=True)
