# shoppingCart
 a simple shopping cart application.

Running
-------
From root directoy

```shell
python3 main.py
```

Tests
-----
```shell
pip install -r requirements.txt
pytest
```

Workflow
--------
```python
checkout = Checkout(pricing_rules=pricing_rules)
checkout.add('VOUCHER')
checkout.add('TSHIRT')
checkout.add('MUG')
price = checkout.get_total()
```

How it works
-----------
1. Creating products `Product(code='VOUCHER', name='Voucher', price=5.0)`
2. `FixedPriceRule(product=mug_product)` for fixed price products.
3. `MultiDiscountRule(product=voucher_product, quantity_multiplier=2, discount_precentage=50)` for 2 for 1 rule. `quantity_multiplier` is for definding the quantity on which to start applying the discount. `discount_precentage` is the discount precentage to apply. E.g: 50%
4. `BulkDiscountRule(product=tshirt_product, min_quantity=3, discount_precentage=5)` for bulk rule. `min_quantity` define quantity to start applying discount from (inclusive). `discount_precentage` is the discount precentage to apply. E.g: 5%


Notes
-----
* The objective of the challange is to see how the pricing rules and calculation are implemented and to check code quality.
* A product can't have more than one rule and if there's a need for a combined rule it should be implemented as a seperate rule.
* Basic Product class and offer Rule have been used to keep everything object oriented and extend on when needed.


