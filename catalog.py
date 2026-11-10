def display_catalog():
    products = {
        1: "Laptop - ₹50000",
        2: "Mobile - ₹20000",
        3: "Headphones - ₹2000"
    }

    print("PRODUCT CATALOGUE")
    for product_id, details in products.items():
        print(product_id, details)


display_catalog()