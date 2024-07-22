from odoo import api, fields, models


class Appointementhospital(models.Model):
    _name = 'hospital.appointement'
    _inherit = ['mail.thread']
    _description = 'hospital appointement'
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", default='New')
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointement = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'OnGoing'), ('done', 'Done'),
                              ('cancel', 'Cancelled')], default='draft', tracking=True)
    appointement_line_ids = fields.One2many('hospital.appointement.lines', 'appointement_id', string="Lines")

    @api.model_create_multi
    def create(self, vals_list):
        print("aasleema", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointement')
        return super(Appointementhospital, self).create(vals_list)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'


class Appointementhospitallines(models.Model):
    _name = 'hospital.appointement.lines'
    _description = 'hospital appointement lines'

    appointement_id = fields.Many2one('hospital.appointement', string="Appointement")
    product_id = fields.Many2one('product.template', string="Product")
    qty = fields.Float(string="Quatity")
