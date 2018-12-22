# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many(
        'openacademy.session', string="Attended Sessions", readonly=True)

# soluciona proble de sessions_id
# https://stackoverflow.com/questions/49900377/odoo-11-0-how-let-res-partner-about-module-tutorial-being-usable
Partner()
