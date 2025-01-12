{
    'name': 'Hospital Management System',
    'author': 'ASMOUCH SOCIETY',
    'license': 'LGPL-3',
    'version': '17.0.1.0',
    'depends': ['mail', 'product'],
    'data': ['security/ir.model.access.csv',
             'data/sequence.xml',
             'views/patients_views.xml',
             'views/patients_readonly_views.xml',
             'views/appointements_views.xml',
             'views/appointements_lines_views.xml',
             'views/patient_tag_views.xml',
             'views/menu.xml', ]
}
