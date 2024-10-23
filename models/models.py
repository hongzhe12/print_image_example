# -*- coding: utf-8 -*-

from odoo import models, fields

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='姓名', required=True)
    age = fields.Integer(string='年龄')
    profile = fields.Binary(string='头像')

