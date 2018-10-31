# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarRequest(models.Model):
    _name = "car.request" # Table in DB => car_request
    _description = "Car Request"

    name = fields.Char(string="Request", required=True, )
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True, )
