import pytest

from src.utils import Category, Product


@pytest.fixture
def product_fixt():
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0, 5
    )


def test_init_product(product_fixt):
    assert product_fixt.name == "Samsung Galaxy S23 Ultra"
    assert product_fixt.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixt.price == 180000.0
    assert product_fixt.quantity == 5


@pytest.fixture
def product_fixt_2():
    return Product(1, 1, "Строка", "Строка")


def test_init_product_2(product_fixt_2):
    assert product_fixt_2.name == 1
    assert product_fixt_2.description != str
    assert product_fixt_2.price == "Строка"
    assert product_fixt_2.quantity != list


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
    assert (
        category_fixt.description == "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_fixt.products == []
    assert category_fixt.category_count == 1
    assert category_fixt.product_count == 0


@pytest.fixture
def category_fixt_2():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        [1, 2, 3],
    )


def test_category_2(category_fixt_2):
    assert category_fixt_2.name == "Смартфоны"
    assert (
        category_fixt_2.description == "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_fixt_2.products == [1, 2, 3]
    assert category_fixt_2.category_count == 2
    assert category_fixt_2.product_count == 3


@pytest.fixture
def category_fixt_3():
    return Category(1, 1, [])


def test_category_3(category_fixt_3):
    assert category_fixt_3.name == 1
    assert category_fixt_3.description == 1
    assert category_fixt_3.products == []
    assert category_fixt_3.category_count == 3
    assert category_fixt_3.product_count == 3


@pytest.fixture
def category_fixt_4():
    return Category(1, 1, ["product"])


def test_category_4(category_fixt_4):
    assert category_fixt_4.name != str
    assert category_fixt_4.description != str
    assert category_fixt_4.products == ["product"]
    assert category_fixt_4.category_count == 4
    assert category_fixt_4.product_count == 4


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
            Product(1,
                    1,
                    "Строка",
                    "Строка"),
        ],
    )


def test_init_category_5(category_fixt_5):
    assert category_fixt_5.name == 2
    assert category_fixt_5.description != str
    assert category_fixt_5.products == [
        Product(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5
        ),
        Product(1, 1, "Строка", "Строка"),
    ]
    assert category_fixt_5.category_count == 5
    assert category_fixt_5.product_count == 6


@pytest.fixture
def category_fixt_6():
    return Category(2, 2, [])


def test_init_category_6(category_fixt_6):
    assert category_fixt_6.name == 2
    assert category_fixt_6.description != str
    assert category_fixt_6.products == []
    assert category_fixt_6.category_count == 6
    assert category_fixt_6.product_count == 6
