from odoo import api
from odoo import fields
from odoo import models
from datetime import date
from dateutil.relativedelta import relativedelta

class Property(models.Model):
    _name = "estate.property"
    _description = "A Property for Real Estate"

    name = fields.Char("Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_avalibility = fields.Date("Date Avalible", copy = False, default=lambda self: date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    gardern_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(selection=[('north','North'),('south','South'),('east','East'),('west','West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('new','New'),('offer_recived','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('cancelled','Cancelled')], default = 'new', copy = False, required = True)


