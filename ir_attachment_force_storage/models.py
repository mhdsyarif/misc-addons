# -*- coding: utf-8 -*-
from openerp import api
from openerp import models


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def _attachment_force_storage(self):
        self.env['ir.attachment'].force_storage()

    @api.model
    def create(self, vals):
        res = super(IrConfigParameter, self).create(vals)
        if vals and vals.get('key') == 'ir_attachment.location':
            self._attachment_force_storage()
        return res

    @api.one
    def write(self, vals):
        res = super(IrConfigParameter, self).write(vals)
        if self.key == 'ir_attachment.location':
            self._attachment_force_storage()
        return res
