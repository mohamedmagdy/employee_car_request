# -*- coding: utf-8 -*-
from odoo import http

class EmployeeCarRequest(http.Controller):

    @http.route('/api/create_car_request', auth='public', csrf=False, type='json', methods=['POST'])
    def create_car_request(self, **kw):
        """Add your own logic"""
        print(http.request)
        print(kw)
        new_car_request = http.request.env['car.request'].sudo().create(kw)

        if new_car_request:
            return "The car request has been created"
        else:
            return "No car request"

    # @http.route('/employee_car_request/employee_car_request/', auth='public')
    # def index(self, **kw):
    #     return "Hello, Odoo Live Session"

#     @http.route('/employee_car_request/employee_car_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_car_request.listing', {
#             'root': '/employee_car_request/employee_car_request',
#             'objects': http.request.env['employee_car_request.employee_car_request'].search([]),
#         })

#     @http.route('/employee_car_request/employee_car_request/objects/<model("employee_car_request.employee_car_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_car_request.object', {
#             'object': obj
#         })