from odoo import models, fields

class Category(models.Model):
    _name= "ticket.category"
    _description = "category"

    name = fields.Char(string="Category" , required=True)
    color = fields.Integer(string="Color")
    description = fields.Text(string="Description")
