from odoo import models, fields, api

class InputDataWizard(models.TransientModel):
    _name = 'input.data.wizard'
    _description = 'Input Data Wizard'

    field1 = fields.Char(string='输入1')
    field2 = fields.Char(string='输入2')

    def action_submit(self):
        print("Field 1:", self.field1)
        print("Field 2:", self.field2)
        return {'type': 'ir.actions.act_window_close'}
