from odoo import models, fields

class Tag(models.Model):
    _name = "ticket.tag"    
    _description = "Tag"

    name = fields.Char(string="Tag", required=True)
    color = fields.Integer(string="Color")