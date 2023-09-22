# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.library_app.controllers.main import Books


class BooksExtended(Books):

    @http.route()
    def booklist(self, **kwargs):
        response = super().booklist(**kwargs)
        if kwargs.get("available"):
            all_books = response.qcontext["books"]
            available_books = all_books.filtered("is_available")
            response.qcontext["books"] = available_books
        
        return response

