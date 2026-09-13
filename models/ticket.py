from odoo import models, fields, api


class TicketTicket(models.Model):
    _name = "ticket.ticket"
    _description = "Support Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Title", default="New Ticket", tracking=True)
    description = fields.Html(string="Description")

    partner_id = fields.Many2one("res.partner", string="Customer", tracking=True)
    user_id = fields.Many2one(
        "res.users",
        string="Assigned To",
        default=lambda self: self.env.user,
        tracking=True,
    )
    category_id = fields.Many2one("ticket.category", string="Category")
    stage_id = fields.Many2one("ticket.stage", string="Stage", tracking=True)
    tag_ids = fields.Many2many("ticket.tag", string="Tags")

    priority = fields.Selection(
        [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")],
        string="Priority",
        default="1",
        tracking=True,
    )

    def action_in_progress(self):
        for record in self:
            if record.stage_id.name == "New" or record.stage_id == 1:
                record.write({"stage_id": 2})

    def action_pending_customer(self):
        for record in self:
            if record.stage_id.name == "In Progress" or record.stage_id == 2:
                record.write({"stage_id": 3})

    def action_resolved(self):
        for record in self:
            if record.stage_id.name == "Pending Customer" or record.stage_id == 3:
                record.write({"stage_id": 4})

    def action_cancelled(self):
        for record in self:
            record.write({"stage_id": 5})

    def action_reset_to_new(self):
        for record in self:
            record.write({"stage_id": 1})
    
    def action_set_new(self):
        for record in self:
            record.write({"stage_id": 1})

