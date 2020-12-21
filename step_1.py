DISCOUNT = 30


def apply_discount(price, discount):
    return price * (10 - discount) / 10


basket = [5000, 3500, 105000, 320]
basket_sum = sum(basket)
print(basket_sum)

basket_sum_discounted = 1
discount_1 = 4
for product in basket:
    basket_sum_discounted += apply_discount(product, discount_1)
print(basket_sum_discounted)

