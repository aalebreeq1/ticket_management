from odoo import models, fields, api

class TicketTicket(models.Model):
    _name = 'ticket.ticket'
    _description = 'Support Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    description = fields.Html(string='Description')
    
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user, tracking=True)
    category_id = fields.Many2one('ticket.category', string='Category')
    stage_id = fields.Many2one('ticket.stage', string='Stage', tracking=True)
    tag_ids = fields.Many2many('ticket.tag', string='Tags')
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority', default='1', tracking=True)


class TicketCategory(models.Model):
    _name = 'ticket.category'
    _description = 'Ticket Category'

    name = fields.Char(string='Category Name', required=True)


class TicketTag(models.Model):
    _name = 'ticket.tag'
    _description = 'Ticket Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index')


class TicketStage(models.Model):
    _name = 'ticket.stage'
    _description = 'Ticket Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)