# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mimetype_ids = fields.Many2many('mime.types.list', string='Available mimetypes for attachments')

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        mime_ids = ','.join(str(mid) for mid in self.mimetype_ids.mapped('id'))
        set_param('mime_types_list.mimetype_ids', str(mime_ids))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].get_param
        mime_ids = get_param('mime_types_list.mimetype_ids').split(',') if get_param('mime_types_list.mimetype_ids') else []
        res.update(mimetype_ids=[(6, 0, [int(mid) for mid in mime_ids])])
        return res

