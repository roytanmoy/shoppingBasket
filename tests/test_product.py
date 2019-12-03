from unittest import TestCase

from core.product import Product


class TestProduct(TestCase):
    def test_create_product(self):
        test_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)

        self.assertEquals(test_product.code, 'VOUCHER')
        assert test_product.name == 'Cabify Voucher'
        assert test_product.price == 5.0