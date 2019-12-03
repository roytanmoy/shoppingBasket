# shoppingBasket
 a simple checkout server and client that communicate over the network.

1. Creating products `Product(code='VOUCHER', name='Cabify Voucher', price=5.0)`
2. `FixedPriceRule(product=mug_product)` for fixed price products.
3. `MultiDiscountRule(product=voucher_product, quantity_multiplier=2, discount_precentage=50)` for 2 for 1 rule. `quantity_multiplier` is for definding the quantity on which to start applying the discount. `discount_precentage` is the discount precentage to apply. E.g: 50%
4. `BulkDiscountRule(product=tshirt_product, min_quantity=3, discount_precentage=5)` for bulk rule. `min_quantity` define quantity to start applying discount from (inclusive). `discount_precentage` is the discount precentage to apply. E.g: 5%


Interface works as specified in challange
```python
checkout = Checkout(pricing_rules=pricing_rules)
checkout.add('VOUCHER')
checkout.add('TSHIRT')
checkout.add('MUG')
price = checkout.get_total()
```

Running
-------
From root directoy

```shell
python3 main.py
```

To run tests
```shell
pip install -r requirements.txt
pytest
```


Assumptions and implements
--------------------------
The code in this repository assumes the following:

* The objective of the challange is to see how the pricing rules and calculation are implemented and to check code quality.
* A product can't have more than one rule and if there's a need for a combined rule it should be implemented as a seperate rule.


The code implements:
* Checkout interface as specified in the challange.
* Basic Product class to keep everything object oriented and extend on when needed.
* Base Rule class to be extended and serve as a base class for all rules.
* Unittests because production code should always have tests.


The code doesn't implement:
* A data store for products and rules isn't included because of the assumptions that the challange's objective is to check design patterns and code quality. A data store should be implemented to avoid hardcoding in real life situations.
* A way to intract with the store without coding isn't included because of the same assumptions as above and the lack of specifications.
