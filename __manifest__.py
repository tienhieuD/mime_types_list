# -*- coding: utf-8 -*-

{
    'name': "Mime Types List",
    'version': '0.1',
    'author': 'Entrust DEV',
    'maintainer': 'Entrust DEV',
    'website': "http://www.odoo.com",
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'sequence': 1000,
    'description': """Long description of Mime Types List module""",
    'summary': """Mime Types List module""",
    'depends': ['base', 'base_setup'],
    'data': [
        'data/mime.types.list.csv',
        'views/mime_types_list_view.xml',
        'views/res_config_setting_view.xml',
    ],
    'demo': [],
    'qweb': [],
    # 'js': ['static/src/js/first_module.js',],
    # 'css': ['static/src/css/web_example.css',],
    # 'images': ['static/description/icon.png',],
    'auto_install': False,
    'application': False,
    'installable': True,
    # 'external_dependencies': {'python' : ['usb.core','serial','qrcode']}
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
}
