from odoo import models, fields

class heroes(models.Model):
    _name = 'lol.heroes' #la info se guarda en la tabla lol_heroes

    name = fields.Char()
    debilidades_id = fields.One2many(comodel_name='lol.debilidades', inverse_name='heroe_id', string="Debilidades")
    batalles_id = fields.One2many(comodel_name='lol.batallas', inverse_name='heroe_id', string="Batalles")

class villanos(models.Model):
    _name = 'lol.villanos' #la info se guarda en la tabla lol_villanos

    name = fields.Char()
    batallas_id = fields.One2many(comodel_name='lol.batallas', inverse_name='villano_id', string="Batallas")

class batallas(models.Model):
    _name = 'lol.batallas' #la info se guarda en la tabla lol_batallas

    name = fields.Char()
    heroe_id = fields.Many2one(comodel_name='lol.heroes', string="Heroe")
    villano_id = fields.Many2one(comodel_name='lol.villanos', string="Villano")
    fecha = fields.Date()
    lugar = fields.Char()

class debilidades(models.Model):
    _name = 'lol.debilidades'

    name = fields.Char()
    intensidad = fields.Integer()
    # add a selection field for skill level
    skill_level = fields.Selection([('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    heroe_id = fields.Many2one(comodel_name='lol.heroes', string="Heroe")


