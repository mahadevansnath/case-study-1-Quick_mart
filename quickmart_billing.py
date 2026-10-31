# quickmart_billing.py

cart = [
    {"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
    {"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
    {"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
    {"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
    {"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]


def line_total(item):
    return item["price"] * item["qty"]


def subtotal(cart):
    return sum(line_total(item) for item in cart)


def apply_discount(amount, percent=0):
    return float(amount - (amount * percent / 100))


def gst(amount, rate=18):
    return float(amount * rate / 100)


def category_totals(cart):

    totals = {}
    for item in cart:
        cat = item["category"]
        totals[cat] = totals.get(cat, 0) + line_total(item)
    return totals


def top_items(cart, n=2):
    sorted_cart = sorted(cart, key=line_total, reverse=True)
    return [item["name"] for item in sorted_cart[:n]]


def print_bill(cart, discount_percent=0):
    print(f"{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}")

    for item in cart:
        total = line_total(item)
        print(f"{item['name']:<10}{item['price']:>6}{item['qty']:>5}{total:>8}")

    sub = subtotal(cart)
    discount_amount = sub * (discount_percent / 100)
    discounted_sub = sub - discount_amount
    tax = gst(discounted_sub, rate=18)
    grand_total = discounted_sub + tax

    print(f"{'Subtotal':<21}{sub:>8.2f}")
    print(f"{f'Discount {discount_percent}%':<21}{discount_amount:>8.2f}")
    print(f"{'GST 18%':<21}{tax:>8.2f}")
    print(f"{'Grand total':<21}{grand_total:>8.2f}")