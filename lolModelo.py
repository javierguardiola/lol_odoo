from odoo import models, fields

class heroes(models.Model):
    _name = 'lol.heroes' #la info se guarda en la tabla test_model2

    name = fields.Char()
    debilidades_id = fields.One2many(comodel_name='lol.debilidades', inverse_name='heroe_id', string="Debilidades")

class debilidades(models.Model):
    _name = 'lol.debilidades'

    name = fields.Char()
    intensidad = fields.Integer()
    heroe_id = fields.Many2one(comodel_name='lol.heroes', string="Heroe")


