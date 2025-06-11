class Product:
    name: str
    description: str
    price: str
    quantity: int

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

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity


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

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return self.__products

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

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
