from odoo import models, fields

class Stage(models.Model):
    _name = "ticket.stage"
    _description = "Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage", required=True, default="New")
    sequence = fields.Integer(string="Sequence", default=10)
    is_closed = fields.Boolean(string="Is Closed")
    fold = fields.Boolean(string='Folded in Kanban', default=False)