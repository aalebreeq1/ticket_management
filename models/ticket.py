from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class TicketTicket(models.Model):
    _name = "ticket.ticket"
    _description = "Support Ticket"
    _inherit = ["approval.record", "mail.thread", "mail.activity.mixin"]

    ticket_ref = fields.Char(
        string="Ticket Reference",
        readonly=True,
        tracking=True,
        copy=False,
        default=lambda self: _("New"),
    )
    title = fields.Char(string="Ticket Title", tracking=True)
    description = fields.Html(string="Description")
    partner_id = fields.Many2one("res.partner", string="Customer", tracking=True)
    user_id = fields.Many2one(
        "res.users",
        string="Assigned To",
        default=lambda self: self.env.user,
        tracking=True,
    )
    category_id = fields.Many2one("ticket.category", string="Category")
    tag_ids = fields.Many2many("ticket.tag", string="Tags")

    # approval_user_ids = fields.Many2many("res.users", string="Approval Users")
    priority = fields.Selection(
        [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")],
        string="Priority",
        default="1",
        tracking=True,
    )
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("ticket_ref", _("New")) == _("New"):
                vals["ticket_ref"] = self.env["ir.sequence"].next_by_code(
                    self._name
                ) or _("New")
        return super().create(vals_list)
