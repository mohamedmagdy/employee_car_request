# -*- coding: utf-8 -*-
from odoo import http

# class EmployeeCarRequest(http.Controller):
#     @http.route('/employee_car_request/employee_car_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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