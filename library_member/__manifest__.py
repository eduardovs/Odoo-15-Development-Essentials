# -*- coding: utf-8 -*-
{
    "name": "Library Member",
    "description": """
        Manage members borrowing books
    """,
    "author": "Daniel Reiis",
    # any module necessary for this one to work correctly
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",

    ],
}
