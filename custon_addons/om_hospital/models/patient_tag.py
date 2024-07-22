from odoo import api, fields, models

class patientTag(models.Model):
    _name ='patient.tag'
    _description ='Patient Tag'


    name = fields.Char(string="Name", required=True )
    sequence= fields.Integer(default=10)
