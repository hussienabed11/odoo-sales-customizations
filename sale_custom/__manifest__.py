{
    'name': 'Sale Customizations',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Customizations for the Sale Order module',
    'description': """
        This module extends the core Sale Order functionality.
        Adds custom fields and prepares for future business logic.
    """,
    'author': 'Hussein',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        # 'security/ir.model.access.csv',  # يمكن إضافته لاحقًا عند الحاجة
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
