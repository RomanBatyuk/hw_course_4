from abc import ABC, abstractmethod


class BaseProduct(ABC):
    __slots__ = ("name", "description", "price", "quantity")

    @abstractmethod
    def new_product(cls, product):
        pass

    def __add__(self, other):
        pass


class Mixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.description}', {self.price}, {self.quantity})"


class Product(Mixin, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

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
        price = float(product["price"])
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Объект должен быть Product")


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

    def middle_price(self):
        counter_price = 0
        for product in self.__products:
            if self.__products != []:
                counter_price += product.price
        try:
            return counter_price // len(self.__products)
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Объeкт должен быть Product")


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Объeкт должен быть Product")


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
