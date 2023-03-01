{
    'name': 'Mediacal Store',
    'version': '1.0.0',
    'category': 'Advance Medical Management App',
    'author': 'manthan',
    'summary': 'Medical Store Management App with advance Search',
    'description': """""",
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/product_view.xml',
        'views/patient_catogory.xml',
        'views/res_users.xml',
        'views/submenu.xml',
        'views/advance_search_template.xml',
        'views/shop_views.xml',
        
        'data/product_public_category.xml',
        'data/products_data.xml',
    ],
    'demo': [],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
}
