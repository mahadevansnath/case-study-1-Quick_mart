# main.py
from quickmart_billing import (
    apply_discount,
    cart,
    category_totals,
    gst,
    line_total,
    print_bill,
    subtotal,
    top_items,
)


def main():
    print("Task 1: Line total")
    print(line_total(cart[0]))
    print()

    print("Task 2: Subtotal")
    print(subtotal(cart))
    print()

    print("Task 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))
    print()

    print("Task 4: GST")
    print(gst(100))
    print(gst(100, 5))
    print()

    print("Task 5: Category totals")
    cat_tot = category_totals(cart)
    for cat in sorted(cat_tot.keys()):
        print(f"{cat:<12}{cat_tot[cat]}")
    print()

    print("Task 6: Top items")
    print(top_items(cart))
    print(top_items(cart, 3))
    print()

    print("Task 7: Bill")
    print_bill(cart, 10)
    print()

    print("Task 8: Tests")
    assert line_total(cart[0]) == 200
    assert apply_discount(200, 50) == 100.0
    assert gst(200) == 36.0
    assert top_items(cart, 1) == ["Notebook"]
    print("All tests passed")


if __name__ == "__main__":
    main()