from odoo import models, fields

class Stage(models.Model):
    _name = "ticket.stage"
    _description = "Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage", required=True, default="New")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_assign', 'Waiting to Assign'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="State", default='draft')
    sequence = fields.Integer(string="Sequence", default=10)
    is_closed = fields.Boolean(string="Is Closed")
    fold = fields.Boolean(string='Folded in Kanban', default=False)