# -*- coding: utf-8 -*-

# import exceptions to use in Python constraints
from odoo import models, fields, api, exceptions


# Modelos (tablas y atributos)


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    # Relaciones entre tablas
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsable", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

    # SQL contrsints
    #     CHECK that the course description and the course title are different
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
    # Make the Course’s name UNIQUE
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)  # Default

    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    active = fields.Boolean(default=True)

    # complex domains. Modify the Session model’s domain
    instructor_id = fields.Many2one('res.partner', string="Instructor",
                                    domain=['|', ('instructor', '=', True),
                                            ('category_id.name', 'ilike', "Teacher")])

    course_id = fields.Many2one(
        'openacademy.course', ondelete='cascade', string="Course", required=True)

    # Using the relational field many2many, modify the Session model to relate every session to
    # a set of attendees.
    # Attendees will be represented by partner records, so we will
    # relate to the built-in model res.partner. Adapt the views accordingly.
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    # Computed fields. Add the percentage of taken seats to the Session model
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    # onchange. Add an explicit onchange to warn about invalid values,
    # like a negative number of seats, or more participants than seats.

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    # Model constraints
    # Add Python constraints
    # # Add a constraint that checks that the instructor is not present in the attendees of his/her own session

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError(
                    "A session's instructor can't be an attendee")


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
                                   string="Attended Sessions", readonly=True)
