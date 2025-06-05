class Product:
    name: str
    description: str
    price: str
    quantity: list

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __eq__(self, other):
        if isinstance(other, Product):
            return (
                self.name == other.name
                and self.description == other.description
                and self.price == other.price
                and self.quantity == other.quantity
            )
        return False

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __eq__(self, other):
        if isinstance(other, Category):
            return (
                self.name == other.name
                and self.description == other.description
                and self.__products == other.__products
            )
        return False

    @property
    def products(self):
        result = []
        for i in self.__products:
            result.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n")
        return "".join(result)

    def add_product(self, new_product: Product):
        if not isinstance(new_product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products_info(self):
        result = []
        for i in self.__products:
            result.append(
                f"{i.name}, {i.description}, {i.price} руб., Остаток: {i.quantity} шт."
            )
        return "\n".join(result)


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
