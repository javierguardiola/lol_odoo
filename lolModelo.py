from odoo import models, fields

class heroes(models.Model):
    _name = 'lol.heroes' #la info se guarda en la tabla test_model2

    name = fields.Char()
    debilidades_id = fields.one2many('lol.debilidades', 'heroe_id', string="Debilidades")

class debilidades(models.Model):
    _name = 'lol.debilidades'

    name = fields.Char()
    intensidad = fields.Integer()
    heroe_id = fields.Many2one('lol.heroes', string="Heroe")


