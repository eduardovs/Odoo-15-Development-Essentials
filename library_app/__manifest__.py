# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "summary": """
        Manage library catalogue and book lending""",
    "author": "Eduardo Vieira",
    "website": "http://pythondev.ca",
    "license": "AGPL-3",
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
        "reports/library_book_report.xml",
    ],
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml",
    ],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "version": "15.0.1.0",
    "application": True,
    "category": "Services/Library",
}
