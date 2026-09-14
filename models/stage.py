from odoo import models, fields
from odoo import api
from odoo.exceptions import ValidationError


class Stage(models.Model):
    _name = "ticket.stage"
    _description = "Stage"
    _order = "sequence, id"

    code = fields.Char(
        string="Code",
        required=True,
        help="this field is for the technical name of the stage avoid using spaces and use lowercase characters only EX: 'new_stage'"
    )
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    is_closed = fields.Boolean(string="Is Closed")
    
