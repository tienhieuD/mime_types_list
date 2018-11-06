# -*- coding: utf-8 -*-
from odoo import fields, models


class MimeTypesList(models.Model):
    _name = 'mime.types.list'
    _rec_name = 'extension'

    name = fields.Char()
    mimetype = fields.Char()
    extension = fields.Char()
