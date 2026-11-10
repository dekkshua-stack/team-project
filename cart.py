def add_to_cart(product, price):
    cart = []
    cart.append({"product": product, "price": price})

    print("Shopping Cart")
    for item in cart:
        print(item["product"], "-", item["price"])

    print("Total:", sum(item["price"] for item in cart))


add_to_cart("Laptop", 50000)