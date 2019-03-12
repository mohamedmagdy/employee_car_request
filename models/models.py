# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CarRequest(models.Model):
    _name = "car.request" # Table in DB => car_request
    _inherit = ['mail.thread']
    _description = "Car Request"

    name = fields.Char(string="Request", required=True, )
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True, )
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                                                         ('validate', 'Validated'), ('refuse', 'Refuse'),
                                                         ('approved', 'Approved'), ], default="draft", track_visibility='onchange', )
    email = fields.Char(string="Email", required=False, )
    website = fields.Char(string="Website", required=False, )

    @api.onchange('email')
    def _onchange_email(self):
        """
        Email: YOURNAME@YOURCOMPANY.COM
        Website: http://www.YOURCOMPANY.COM
        :return:
        """
        # return {
        #     'domain': {'other_id': [('partner_id', '=', partner_id)]},
        #     'warning': {'title': "Warning", 'message': "What is this?"},
        # }
        result = {}
        if self.email:
            # self.website = 'http://www.%s' % (self.email.split('@')[1])
            result.update({
                'value': {
                    'website': 'http://www.%s' % (self.email.split('@')[1])
                },
                'warning': {
                    'title': 'Congrates!',
                    'message': 'You have added an email!',
                },
                'domain': {
                    'employee_id': [('id', '!=', 20)],
                }
            })

        return result

    # _sql_constraints is working on DB level and you can find it in the table:
    # \d TABLE_NAME
    # SQL Constraints can use to rules: unique & check
    _sql_constraints = [
        ('unique_email', 'unique(email)', 'The email should be unique!'),
    ]

    @api.constrains('email')
    def _check_email(self):
        """
        Constrains will check / triggered for the listed fields only in creation and updating.
        @api.constraints will work on the application level
        :return:
        """
        if self.email.endswith('gmail.com'):
            raise ValidationError("Gmail is not accepted!")
        if self.email.endswith('yahoo.com'):
            raise ValidationError("Yahoo is not accepted!")

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'

    @api.multi
    def validate_request(self):
        self.state = 'validate'

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'
