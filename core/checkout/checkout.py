class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules

        # Dict with codes as keys and a rule as value
        self.available_products = {}

        for rule in pricing_rules:
            if rule.product.code not in self.available_products.keys():
                self.available_products[rule.product.code] = rule
            else:
                raise Exception('Can\'t add more than one pricing rule for a product')

        self.bought_products = []

    def add(self, code):
        if code in self.available_products.keys():
            self.bought_products.append(code)
        else:
            raise Exception('Product code does not exist')

    def get_total(self):
        total_price = 0
        for code in set(self.bought_products):
            quantity = self.bought_products.count(code)

            rule = self.available_products[code]
            total_price += rule.apply(quantity)

        return total_price