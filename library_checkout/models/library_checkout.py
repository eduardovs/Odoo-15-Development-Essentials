from odoo import api, fields, models


class Checkout(models.Model):
    _name = "library.checkout"
    _description = "Checkout Request"

    member_id = fields.Many2one("library.member", required=True)
    user_id = fields.Many2one("res.users", "Librarian", default=lambda s: s.env.user)
    request_date = fields.Date(default = lambda s: fields.Date.today(),
                               compute="_compute_request_date_onchange",
                               store=True,
                               readonly=False,)
    line_ids = fields.One2many(
        "library.checkout.line",
        "checkout_id",
        string="Borrowed Books",
    )

    @api.model
    def _default_stage_id(self):
        Stage = self.env["library.checkout.stage"]
        return Stage.search([("state", "=", "new")], limit=1)
    
    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)
    
    @api.depends("member_id")
    def _compute_request_date_onchange(self):
        today_date = fields.Date.today()
        if self.request_date != today_date:
            self.request_date = today_date
            return {
                "warning": {
                    "title": "Change Request Date",
                    "message": "Request date changed to today!"
                }
            }
    
    
    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date()


    def write(self, vals):
        # Code before write: `self` has the old values
        old_state = self.stage_id.state
        super().write(vals)
        # Code after write: can use `self` with the updated values
        new_state = self.stage_id.state
        if not self.env.context.get("_checkout_write"):
            if new_state != old_state and new_state == "open":
                self.with_context(_checkout_write=True).write(
                    {"checkout_date": fields.Date.today()})
            if new_state != old_state and new_state == "done":
                self.with_context(_checkout_write=True).write(
                    {"close_date": fields.Date.today()})
        return True
    




