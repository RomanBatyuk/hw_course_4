import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_fixt():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


def test_init_product(product_fixt):
    assert product_fixt.name == "Samsung Galaxy S23 Ultra"
    assert product_fixt.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixt.price == 180000.0
    assert product_fixt.quantity == 5


@pytest.fixture
def product_fixt_2():
    return Product(1, 1, "Строка", 10)


def test_init_product_2(product_fixt_2):
    assert product_fixt_2.name == 1
    assert not isinstance(product_fixt_2.description, str)
    assert product_fixt_2.price == "Строка"
    assert isinstance(product_fixt_2.quantity, int)


@pytest.fixture
def category_fixt():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        [],
    )


def test_category(category_fixt):
    assert category_fixt.name == "Смартфоны"
    assert category_fixt.description == (
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_fixt.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


@pytest.fixture
def category_fixt_2():
    products = [
        Product("Prod1", "Desc1", 100, 1),
        Product("Prod2", "Desc2", 200, 2),
        Product("Prod3", "Desc3", 300, 3),
    ]
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        products,
    )


def test_category_2(category_fixt_2):
    assert category_fixt_2.name == "Смартфоны"
    assert category_fixt_2.description == (
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_fixt_2.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


@pytest.fixture
def category_fixt_3():
    return Category(1, 1, [])


def test_category_3(category_fixt_3):
    assert category_fixt_3.name == 1
    assert category_fixt_3.description == 1
    assert category_fixt_3.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


@pytest.fixture
def category_fixt_4():
    return Category(1, 1, [Product("product", "desc", 100, 1)])


def test_category_4(category_fixt_4):
    assert category_fixt_4.name != str
    assert category_fixt_4.description != str
    assert len(category_fixt_4.products) == 1
    assert isinstance(category_fixt_4.products[0], Product)
    assert Category.category_count == 1
    assert Category.product_count == 1


@pytest.fixture
def category_fixt_5():
    return Category(
        2,
        2,
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product(1, 1, "Строка", 10),
        ],
    )


def test_init_category_5(category_fixt_5):
    assert category_fixt_5.name == 2
    assert category_fixt_5.description != str
    assert len(category_fixt_5.products) == 2
    assert isinstance(category_fixt_5.products[0], Product)
    assert isinstance(category_fixt_5.products[1], Product)
    assert Category.category_count == 1
    assert Category.product_count == 2


@pytest.fixture
def category_fixt_6():
    return Category(2, 2, [])


def test_init_category_6(category_fixt_6):
    assert category_fixt_6.name == 2
    assert category_fixt_6.description != str
    assert category_fixt_6.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(category_fixt):
    product = Product("iPhone 14", "128GB, Черный цвет", 150000.0, 10)
    category_fixt.add_product(product)
    assert Category.product_count == 1
    assert len(category_fixt.products) == 1
    assert isinstance(category_fixt.products[0], Product)


def test_add_product_invalid_type(category_fixt):
    with pytest.raises(TypeError):
        category_fixt.add_product("Not a Product")


def test_product_quantity_update(product_fixt):
    product_fixt.quantity = 10
    assert product_fixt.quantity == 10


def test_category_products_info(category_fixt_2):
    expected_info = (
        "Prod1, Desc1, 100 руб., Остаток: 1 шт.\n"
        "Prod2, Desc2, 200 руб., Остаток: 2 шт.\n"
        "Prod3, Desc3, 300 руб., Остаток: 3 шт."
    )
    assert category_fixt_2.products_info == expected_info


def test_category_empty_products_info(category_fixt):
    assert category_fixt.products_info == ""


def test_product_str(product_fixt):
    assert str(product_fixt) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category_fixt_2):
    assert str(category_fixt_2) == "Смартфоны, количество продуктов: 6 шт."


def test_product_add(product_fixt):
    product2 = Product("iPhone 15", "128GB", 200000.0, 3)
    total_value = product_fixt + product2
    assert total_value == 180000.0 * 5 + 200000.0 * 3


def test_product_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 1000.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_product_eq(product_fixt):
    same_product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product_fixt == same_product
