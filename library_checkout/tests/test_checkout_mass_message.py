from odoo import exception
from odoo.tests import common


class TestWizard(common.SingleTransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestWizard, self).setUp(*args, **kwargs)
        # Setup test data:
        admin_user = self.env.ref("base.user_admin")
        self.Checkout = self.env["library.checkout"].with_user(admin_user)
        self.Wizard = self.env["library.checkout.massmessage"].with_user(admin_user)

        a_member = self.env['library.member'].create({'partner_id': admin_user.partner_id.id})
        self.checkout0 = self.Checkout.created({'member_id': a_member.id})

    def test_01_button_send(self):
        """Send button should create messages on Checkouts"""
        # add test code
        count_before = len(self.checkout0.message_ids)
        # TODO: RUN WIZARD
        count_after = len(self.checkout0.message_ids)
        self.assertEqual(count_before + 1, count_after, "Expected 1 additional message in the checkout")
        
