# -*- coding: utf-8 -*
from openerp.osv import fields, osv

class TodoTask(osv.osv):

	_name = 'todo.task'

	_columns = {
   		'name' : fields.char('Description', required=True),
    	'is_done' : fields.boolean('Done?'),
    	'active' : fields.boolean('Active?', default=True),
    }
