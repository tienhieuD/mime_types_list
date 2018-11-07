# -*- coding: utf-8 -*-
import json

from odoo import http, _
from odoo.http import request
from odoo.addons.web.controllers.main import Binary, serialize_exception


class Binary(Binary):
    def check_accepted_file(self, file):
        available_mimetype = request.env['ir.config_parameter'].sudo().get_param('mime_types_list.mimetype_ids')
        if available_mimetype:
            mimetype_ids = request.env['mime.types.list'].sudo().browse([int(mid) for mid in available_mimetype.split(',')])
            mimetype_accepted = mimetype_ids.mapped(lambda r: (r.mimetype, r.extension))
            file_mimetype = (file.mimetype, '.%s' % file.filename.split('.')[-1])
            return file_mimetype in mimetype_accepted

    def get_error_response(self, callback, args):
        return """
        <script language="javascript" type="text/javascript">
            var win = window.top.window;
            win.jQuery(win).trigger(%s, %s);
        </script>""" % (json.dumps(callback), json.dumps(args))

    @http.route()  # '/web/binary/upload', type='http', auth="user"
    @serialize_exception
    def upload(self, callback, ufile):
        if self.check_accepted_file(ufile):
            return super(Binary, self).upload(callback, ufile)
        return self.get_error_response(callback, [False, _("Định dạng file không cho phép")])

    @http.route()  # '/web/binary/upload_attachment', type='http', auth="user"
    @serialize_exception
    def upload_attachment(self, callback, model, id, ufile):
        if self.check_accepted_file(ufile):
            return super(Binary, self).upload_attachment(callback, model, id, ufile)
        return self.get_error_response(callback, [{'error': _("Định dạng file không cho phép")}])
