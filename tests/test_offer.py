from unittest import TestCase

from core.offer import FixedPriceRule, MultiDiscountRule, BulkDiscountRule
from core.product import Product


class TestFixedPriceRule(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)

    def test_ok(self):
        rule = FixedPriceRule(product=self.test_product)

        self.assertEquals(rule.apply(0), 0.0)
        self.assertEquals(rule.apply(1), 5.0)
        self.assertEquals(rule.apply(2), 10.0)


class TestMultiDiscountRule(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)

    def test_ok(self):
        rule = MultiDiscountRule(product=self.test_product, quantity_multiplier=2, discount_precentage=50)

        self.assertEquals(rule.apply(0), 0.0)
        self.assertEquals(rule.apply(1), 5.0)
        self.assertEquals(rule.apply(2), 5.0)
        self.assertEquals(rule.apply(3), 10.0)
        self.assertEquals(rule.apply(100), 250.0)


class TestBulkDiscountRule(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)

    def test_ok(self):
        rule = BulkDiscountRule(product=self.test_product, min_quantity=3, discount_precentage=5)

        self.assertEquals(rule.apply(0), 0.0)
        self.assertEquals(rule.apply(1), 5.0)
        self.assertEquals(rule.apply(2), 10.0)
        self.assertEquals(rule.apply(3), 14.25)
        self.assertEquals(rule.apply(100), 475.0)