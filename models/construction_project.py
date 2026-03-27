from odoo import api, fields, models, exceptions


class ConstructionProject(models.Model):
    _name = 'construction.project'
    _description = 'Projects'

    project_name = fields.Char(string='Project Name', required=True)
    project_code = fields.Char(string='Project Code')
    customer = fields.Char(string='Customer')
    project_manager = fields.Many2one('res.users', string='Project Manager')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    budget = fields.Float(string='Budget', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('close', 'Close'),
    ], string='State', default='draft', required=True)
    description = fields.Text(string='Description', required=True)

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            if rec.state != 'done':
                rec.state = 'done'

    def action_close(self):
        for rec in self:
            rec.state = 'close'