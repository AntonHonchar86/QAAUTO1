import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    # assert len(orders) == 1

    # Check stucture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_insert_user(database):
    database.insert_user(3, "Anton", "Svitla, 6", "Kyiv", "1212", "Ukraine")
    customers = database.get_detailed_customers_by_id(3)
    assert customers[0][0] == 3
    assert customers[0][1] == "Anton"
    assert customers[0][2] == "Svitla, 6"
    assert customers[0][3] == "Kyiv"
    assert customers[0][4] == "1212"
    assert customers[0][5] == "Ukraine"


@pytest.mark.database
def test_wrong_type_data_user_insert(database):
    database.insert_user(4, 1, 2.0, True, 4, 5)
    customers = database.get_detailed_customers_by_id(4)
    # Перевірка, що в таблицю можна вносити некоректні типи даних
    assert type(customers[0][1]) != type(1)
    assert type(customers[0][2]) != type(2.0)
    assert type(customers[0][3]) != type(True)
    assert type(customers[0][4]) != type(4)
    assert type(customers[0][5]) != type(5)


@pytest.mark.database
def test_wrong_type_data_product_insert(database):
    database.insert_product(5, False, 2.0, "22")
    products = database.get_detailed_products_by_id(5)
    # Перевірка, що в стовбці таблиці можна вносити некоректні типи даних
    assert type(products[0][1]) != type(False)
    assert type(products[0][2]) != type(2.0)
    assert type(products[0][3]) != type("22")


@pytest.mark.database
def test_user_delete_by_id(database):
    database.insert_user(5, "Ivan", "Street", "City", "111", "Country")
    database.delete_user_by_id(5)
    user = database.get_detailed_customers_by_id(5)
    assert len(user) == 0


@pytest.mark.database
def test_insert_order(database):
    database.insert_orders(2, 2, 2, "12:12:12")
    orders = database.get_orders_by_id(2)
    detailed_orders = database.get_detailed_orders()
    assert orders[0][0] == 2
    assert orders[0][1] == 2
    assert orders[0][2] == 2
    assert orders[0][3] == "12:12:12"
    assert detailed_orders[1][1] == "Stepan"


@pytest.mark.database
def test_wrong_type_data_orders_insert(database):
    database.insert_orders(3, 2.0, True, "12:12:12")
    orders = database.get_orders_by_id(3)
    # Перевірка, що в стовбці таблиці можна вносити некоректні типи даних
    assert type(orders[0][1]) != type(2.0)
    assert type(orders[0][2]) != type(True)


@pytest.mark.database
def test_order_delete_by_id(database):
    database.insert_orders(4, 2, 2, "11:11:11")
    database.delete_order_by_id(4)
    order = database.get_orders_by_id(4)
    assert len(order) == 0


@pytest.mark.database
def test_check_add_wrong_id_to_orders(database):
    # Перевірка, що в таблицю orders можна внести дані з неіснуючим зовнішним ключем
    database.insert_orders(4, 8, 1, "12:12:12")
    list = database.get_customers_id()
    print(list)
    # detailed_orders = db.get_detailed_orders()
    cust_id = database.get_customers_id_from_orders_by_id(4)
    print(cust_id)
    assert cust_id[0] not in list
