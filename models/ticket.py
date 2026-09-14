from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class TicketTicket(models.Model):
    _name = "ticket.ticket"
    _description = "Support Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    ticket_id = fields.Char(
        string="Ticket ID",
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
    stage_id = fields.Many2one("ticket.stage", string="Stage", tracking=True)
    stage_code=fields.Char(string="Stage Name", related="stage_id.code", store=True)
    tag_ids = fields.Many2many("ticket.tag", string="Tags")

    priority = fields.Selection(
        [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")],
        string="Priority",
        default="1",
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("ticket_id", _("New")) == _("New"):
                vals["ticket_id"] = self.env["ir.sequence"].next_by_code(
                    "ticket.ticket"
                ) or _("New")
        return super().create(vals_list)

    def _set_stage(self, code):
        stage = self.env["ticket.stage"].search([("code", "=", code)], limit=1)
        if stage:
            self.write({"stage_id": stage.id})

    def action_draft(self):
        for record in self:
            record._set_stage("draft")

    def action_new(self):
        for record in self:
            if record.stage_code == "draft":
                record._set_stage("new")

    def action_in_progress(self):
        for record in self:
            if record.stage_code == "new":
                record._set_stage("in_progress")

    def action_resolved(self):
        for record in self:
            if record.stage_code == "in_progress":
                record._set_stage("resolved")

    def action_cancelled(self):
        for record in self:
            record._set_stage("cancelled")

    def action_reset_to_draft(self):
        for record in self:
            if record.stage_code in ("resolved", "cancelled"):
                record._set_stage("draft")
