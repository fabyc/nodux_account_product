#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
import copy

from trytond.model import ModelSQL, fields
from trytond.pyson import Eval, Or
from trytond import backend
from trytond.transaction import Transaction
from trytond.pool import PoolMeta

__all__ = ['Category', 'Template', 'MissingFunction']
__metaclass__ = PoolMeta

class MissingFunction(fields.Function):
    '''Function field that will raise the error
    when the value is accessed and is None'''

    def __init__(self, field, error, getter, setter=None, searcher=None,
            loading='lazy'):
        super(MissingFunction, self).__init__(field, getter, setter=setter,
            searcher=searcher, loading=loading)
        self.error = error

    def __copy__(self):
        return MissingFunction(copy.copy(self._field), self.error, self.getter,
            setter=self.setter, searcher=self.searcher)

    def __deepcopy__(self, memo):
        return MissingFunction(copy.deepcopy(self._field, memo), self.error,
            self.getter, setter=self.setter, searcher=self.searcher)

    def __get__(self, inst, cls):
        value = super(MissingFunction, self).__get__(inst, cls)
        if inst is not None and value is None:
            inst.raise_user_error(self.error, (inst.name, inst.id))
        return value

class Category:
    __name__ = 'product.category'
    account_revenue_no_iva = fields.Property(fields.Many2One('account.account',
            'Ventas no grabadas de Impuesto', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_revenue_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Ventas no grabadas de Impuesto'), 'missing_account', 'get_account')

    account_devolucion_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Venta gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_devolucion_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Venta gravadas'), 'missing_account', 'get_account')

    account_devolucion_no_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Venta no gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_devolucion_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Venta no gravadas'), 'missing_account', 'get_account')

    account_descuento_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Venta gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_descuento_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Venta gravadas'), 'missing_account', 'get_account')

    account_descuento_no_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Venta no gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_descuento_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Venta no gravadas'), 'missing_account', 'get_account')

    account_expense_no_iva = fields.Property(fields.Many2One('account.account',
            'Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_expense_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Compras no Gravadas'), 'missing_account', 'get_account')


    account_expense_devolucion_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Compras Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_expense_devolucion_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Compras Gravadas'), 'missing_account', 'get_account')

    account_expense_devolucion_no_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_expense_devolucion_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Compras no Gravadas'), 'missing_account', 'get_account')

    account_expense_descuento_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Compras Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_expense_descuento_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Compras Gravadas'), 'missing_account', 'get_account')

    account_expense_descuento_no_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_parent')),
                },
            depends=['account_parent']))

    account_expense_descuento_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Compras no Gravadas'), 'missing_account', 'get_account')

class Template:
    __name__ = 'product.template'

    account_revenue_no_iva = fields.Property(fields.Many2One('account.account',
            'Ventas no grabadas de Impuesto', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_revenue_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Ventas no grabadas de Impuesto'), 'missing_account', 'get_account')

    account_devolucion_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Venta gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_devolucion_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Venta gravadas'), 'missing_account', 'get_account')

    account_devolucion_no_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Venta no gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_devolucion_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Venta no gravadas'), 'missing_account', 'get_account')

    account_descuento_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Venta gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_descuento_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Venta gravadas'), 'missing_account', 'get_account')

    account_descuento_no_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Venta no gravadas', domain=[
                ('kind', '=', 'revenue'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_descuento_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Venta no gravadas'), 'missing_account', 'get_account')

    account_expense_no_iva = fields.Property(fields.Many2One('account.account',
            'Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_expense_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Compras no Gravadas'), 'missing_account', 'get_account')


    account_expense_devolucion_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Compras Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_expense_devolucion_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Compras Gravadas'), 'missing_account', 'get_account')

    account_expense_devolucion_no_iva = fields.Property(fields.Many2One('account.account',
            'Devolucion Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_expense_devolucion_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Devolucion Compras no Gravadas'), 'missing_account', 'get_account')

    account_expense_descuento_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Compras Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_expense_descuento_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Compras Gravadas'), 'missing_account', 'get_account')

    account_expense_descuento_no_iva = fields.Property(fields.Many2One('account.account',
            'Descuento Compras no Gravadas', domain=[
                ('kind', '=', 'expense'),
                ('company', '=', Eval('context', {}).get('company', -1)),
                ],
            states={
                'invisible': (~Eval('context', {}).get('company')
                    | Eval('account_category')),
                },
            depends=['account_category']))

    account_expense_descuento_no_iva_used = MissingFunction(fields.Many2One('account.account',
            'Descuento Compras no Gravadas'), 'missing_account', 'get_account')

    @classmethod
    def __setup__(cls):
        super(Template, cls).__setup__()
