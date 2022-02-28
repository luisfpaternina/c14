{
    'name': 'SAT COMPANIES SUSCRIPTION',

    'version': '14.0.1',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'stock',

    'depends': [

        'sat_companies',
        'sale_subscription',
        'sat_companies_sale',
        'sat_companies_stock',
        'sat_companies_project',
        'contacts',
        'sale_management'
    ],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        'data/stock.gadgets.contract.type.csv',
        'data/subscription.reason.change.csv',
        'data/subscription.inspection.report.csv',
        'data/product_template_data.xml',
        'views/sale_suscription_template_view.xml',
        'views/sale_order_template.xml',
        'views/sale_subscription.xml',
        'views/sale_order_view.xml',
        'views/res_partner.xml',
        'views/sale_subscription_demand.xml',
        'views/subscription_reason_change.xml',
        'views/subscription_inspection_report.xml',
        
    ],
    'installable': True
}
