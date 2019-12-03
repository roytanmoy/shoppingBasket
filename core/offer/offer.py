from ..product import Product


class Rule:
    def __init__(self, product: Product):
        self.product = product



class FixedPriceRule(Rule):

    def apply(self, quantity):
        return quantity * self.product.price


class MultiDiscountRule(Rule):
    def __init__(self, product, quantity_multiplier, discount_precentage):
        super(MultiDiscountRule, self).__init__(product)

        self.quantity_multiplier = quantity_multiplier
        self.discount_precentage = discount_precentage

        # Calculate discounted price
        discount = self.product.price * (self.discount_precentage / 100)
        self.discounted_price = self.product.price - discount

    def apply(self, quantity):
        discounted_quantity = (quantity // self.quantity_multiplier) * self.quantity_multiplier
        normal_price_quantity = quantity - discounted_quantity

        return (normal_price_quantity * self.product.price) + (discounted_quantity * self.discounted_price)


class BulkDiscountRule(Rule):
    def __init__(self, product, min_quantity, discount_precentage):
        super(BulkDiscountRule, self).__init__(product)

        self.min_quantity = min_quantity
        self.discount_precentage = discount_precentage

        # Calculate discounted price
        discount = self.product.price * (self.discount_precentage / 100)
        self.discounted_price = self.product.price - discount

    def apply(self, quantity):
        if quantity >= self.min_quantity:
            return quantity * self.discounted_price

        return quantity * self.product.price