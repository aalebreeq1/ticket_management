from odoo import models, fields
from odoo import api
from odoo.exceptions import ValidationError


class Tag(models.Model):
    _name = "ticket.tag"
    _description = "Tag"

    code = fields.Char(
        string="Code",
        required=True,
        help="this field is for the technical name of the tag avoid using spaces and use lowercase characters only EX: 'new_tag'"
    )
    name = fields.Char(string="Tag", required=True)
    color = fields.Integer(string="Color")
    

