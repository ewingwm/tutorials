from odoo import models
from odoo import fields

class Property_Type(models.Model):
    _name = "estate.property.type"
    _description ="Types of properties for the Real Estate Module"

    name = fields.Char(required = True)

