# -*- coding: utf-8 -*-
# from odoo import http


# class Enterprise(http.Controller):
#     @http.route('/enterprise/enterprise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enterprise/enterprise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enterprise.listing', {
#             'root': '/enterprise/enterprise',
#             'objects': http.request.env['enterprise.enterprise'].search([]),
#         })

#     @http.route('/enterprise/enterprise/objects/<model("enterprise.enterprise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enterprise.object', {
#             'object': obj
#         })
