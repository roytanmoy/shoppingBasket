from core.checkout import Checkout
from core.product import Product
from core.offer import FixedPriceRule, MultiDiscountRule, BulkDiscountRule

voucher_product = Product(code='VOUCHER', name='Cabify Voucher', price=5.0)
tshirt_product = Product(code='TSHIRT', name='Cabify T-Shirt', price=20.0)
mug_product = Product(code='MUG', name='Cabify Coffee Mug', price=7.50)

pricing_rules = [
    FixedPriceRule(product=mug_product),
    MultiDiscountRule(product=voucher_product, quantity_multiplier=2, discount_precentage=50),
    BulkDiscountRule(product=tshirt_product, min_quantity=3, discount_precentage=5)
]

if __name__ == '__main__':
    checkout = Checkout(pricing_rules=pricing_rules)
    checkout.add('VOUCHER')
    checkout.add('TSHIRT')
    checkout.add('MUG')
    price = checkout.get_total()

    print('Items: {}'.format(', '.join(checkout.bought_products)))
    print('Total: {}€'.format(price))
    print('\n')

    checkout = Checkout(pricing_rules=pricing_rules)
    checkout.add('VOUCHER')
    checkout.add('TSHIRT')
    checkout.add('VOUCHER')
    price = checkout.get_total()

    print('Items: {}'.format(', '.join(checkout.bought_products)))
    print('Total: {}€'.format(price))
    print('\n')

    checkout = Checkout(pricing_rules=pricing_rules)
    checkout.add('TSHIRT')
    checkout.add('TSHIRT')
    checkout.add('TSHIRT')
    checkout.add('VOUCHER')
    checkout.add('TSHIRT')
    price = checkout.get_total()

    print('Items: {}'.format(', '.join(checkout.bought_products)))
    print('Total: {}€'.format(price))
    print('\n')

    checkout = Checkout(pricing_rules=pricing_rules)
    checkout.add('VOUCHER')
    checkout.add('TSHIRT')
    checkout.add('VOUCHER')
    checkout.add('VOUCHER')
    checkout.add('MUG')
    checkout.add('TSHIRT')
    checkout.add('TSHIRT')
    price = checkout.get_total()

    print('Items: {}'.format(', '.join(checkout.bought_products)))
    print('Total: {}€'.format(price))
    print('\n')