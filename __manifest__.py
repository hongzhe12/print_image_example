# -*- coding: utf-8 -*-
{
    'name': "student_management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/paperformat_view.xml',  # 引入纸张格式视图文件
        'views/report_action_view.xml',  # 引入报告动作视图文件
        'views/report_template.xml',  # 引入报告模板文件
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
