from odoo import models, fields
from odoo import api
from odoo.exceptions import ValidationError


class Category(models.Model):
    _name = "ticket.category"
    _description = "category"

    code = fields.Char(
        string="Code",
        required=True,
        help="this field is for the technical name of the category avoid using spaces and use lowercase characters only EX: 'new_category'",
    )
    name = fields.Char(string="Category", required=True)
    color = fields.Integer(string="Color")
    description = fields.Text(string="Description")
    
