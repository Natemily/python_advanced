def print_products(*args):
    products = [arg for arg in args if isinstance(arg, str) and arg]

    if not products:
        print("Нет продуктов")
    else:
        for i, product in enumerate(products, start=1):
            print(f"{i}) {product}")