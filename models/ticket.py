from odoo import models, fields, api, _


class TicketTicket(models.Model):
    _name = "ticket.ticket"
    _description = "Support Ticket"
    _inherit = ["approval.record", "mail.thread", "mail.activity.mixin"]
    _rec_name = "ticket_ref"

    ticket_ref = fields.Char(
        string="Ticket Reference",
        readonly=True,
        tracking=True,
        copy=False,
        index=True,
        default=lambda self: _("New"),
    )
    title = fields.Char(string="Ticket Title", required=True, tracking=True)
    description = fields.Html(string="Description", required=True)
    partner_id = fields.Many2one(
        "res.company", string="Company", tracking=True, required=True
    )

    responsible_manager_id = fields.Many2one(
        "res.users",
        string="Responsible Manager",
        tracking=True,
        required=True,
        default=lambda self: self.env.user,
        readonly=True,
    )
    user_id = fields.Many2one(
        "res.users",
        string="Assigned To",
        tracking=True,
        required=True,
        domain=lambda self: [
            ("group_ids", "in", self.env.ref("ticket_management.group_ticket_user").id)
        ],
    )
    category_id = fields.Many2one("ticket.category", string="Category", required=True)
    tag_ids = fields.Many2many("ticket.tag", string="Tags", required=True)

    approval_user_ids = fields.Many2many("res.users", string="Approval Users")

    priority = fields.Selection(
        [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")],
        string="Priority",
        default="1",
        tracking=True,
    )

    start_date = fields.Datetime(
        string="Start Date",
        readonly=True,
        help="The start date will be set when the ticket state moved to  In Progress",
    )

    end_date = fields.Datetime(
        string="End Date",
        readonly=True,
        help="The end date will be set when the ticket state moved to resolved",
    )
    duration_in_hours = fields.Float(
        string="Duration (Hours)",
        readonly=True,
        compute="_compute_duration_in_hours",
        help="The duration will be calculated based on the start and end dates",
    )

    def set_start_date(self):
        for record in self:
            if record.state == "in_progress" and not record.start_date:
                record.start_date = fields.Datetime.now()
                record.end_date = None
                record.duration_in_hours = None

    def set_end_date(self):
        for record in self:
            if record.state in ["resolved", "approved"] and not record.end_date:
                record.end_date = fields.Datetime.now()

    def write(self, vals):
        res = super().write(vals)
        if "state" in vals:
            if vals["state"] == "in_progress":
                self.set_start_date()
            elif vals["state"] in ["resolved", "approved"]:
                self.set_end_date()
        return res

    @api.depends("start_date", "end_date")
    def _compute_duration_in_hours(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration_in_hours = (
                    record.end_date - record.start_date
                ).total_seconds() / 3600
            else:
                record.duration_in_hours = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("ticket_ref") or vals.get("ticket_ref") == _("New"):
                vals["ticket_ref"] = self.env["ir.sequence"].next_by_code(
                    self._name
                ) or _("New")
        return super().create(vals_list)
