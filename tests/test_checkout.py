from unittest import TestCase

from core.offer import FixedPriceRule, MultiDiscountRule, BulkDiscountRule
from core.product import Product
from core.checkout import Checkout


class TestFixedPriceRule(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)

        cls.test_rule = FixedPriceRule(product=cls.test_product)

    def test_create_ok(self):
        checkout = Checkout([self.test_rule])

        self.assertEquals(checkout.available_products, {'VOUCHER': self.test_rule})

    def test_create_ko(self):
        with self.assertRaisesRegex(Exception, 'Can\'t add more than one pricing rule for a product'):
            Checkout([self.test_rule, self.test_rule])

    def test_add_ok(self):
        checkout = Checkout([self.test_rule])
        checkout.add('VOUCHER')

        self.assertEquals(checkout.bought_products, ['VOUCHER'])

    def test_add_multiple(self):
        checkout = Checkout([self.test_rule])
        checkout.add('VOUCHER')
        checkout.add('VOUCHER')
        checkout.add('VOUCHER')

        self.assertEquals(checkout.bought_products, ['VOUCHER', 'VOUCHER', 'VOUCHER'])

    def test_add_ko(self):
        checkout = Checkout([self.test_rule])

        with self.assertRaisesRegex(Exception, 'Product code does not exist'):
            checkout.add('NONE')

    def test_total(self):
        tshirt_product = Product(code='TSHIRT', name='Cabify T-Shirt', price=20.0)
        mug_product = Product(code='MUG', name='Cabify Coffee Mug', price=7.50)

        pricing_rules = [
            FixedPriceRule(product=mug_product),
            MultiDiscountRule(product=self.test_product, quantity_multiplier=2, discount_precentage=50),
            BulkDiscountRule(product=tshirt_product, min_quantity=3, discount_precentage=5)
        ]

        checkout = Checkout(pricing_rules)
        checkout.add('VOUCHER')
        checkout.add('TSHIRT')
        checkout.add('VOUCHER')
        checkout.add('VOUCHER')
        checkout.add('MUG')
        checkout.add('TSHIRT')
        checkout.add('TSHIRT')

        self.assertEquals(checkout.get_total(), 74.5)