{
    'name': 'Real Estate',
    'depends': [
        'base',
    ],
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        "views/estate_property_types_views.xml",
        'views/estate_menus.xml'
    ],
    'license': 'LGPL-3',
}
