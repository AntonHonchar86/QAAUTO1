import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"D:\\courses\\qa auto\\git\\qaauto1" + "\\chromdriver.exe")
    )

    # відкриваю сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Умулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваю браузер
    driver.close()


# Individual tests


@pytest.mark.ui1
def test_check_Wiki():
    driver = webdriver.Chrome(
        service=Service(r"D:\\courses\\qa auto\\git\\qaauto1" + "\\chromdriver.exe")
    )

    # Open the Wikipedia page
    driver.get(
        "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"
    )

    # Find "Log In" button and emulate a mouse click
    btn_elem = driver.find_element(By.ID, "pt-login")
    btn_elem.click()

    # Find field for Username and enter Username
    user_elem = driver.find_element(By.ID, "wpName1")
    user_elem.send_keys("Antonio cassano86")

    # Find field for Password and enter Password
    pass_elem = driver.find_element(By.ID, "wpPassword1")
    pass_elem.send_keys(".dtynec86")

    # Find "Log in" button and emulate a mouse click
    btn1_elem = driver.find_element(By.NAME, "wploginattempt")
    btn1_elem.click()

    # Check that the name of the page is what we expect
    assert driver.title == "Вікіпедія"

    # Find Search field and enter Search word
    search_elem = driver.find_element(By.NAME, "search")
    search_elem.send_keys("Україна")

    # Find Search button and emulate a mouse click
    btn2_elem = driver.find_element(By.ID, "searchButton")
    btn2_elem.click()

    # Check that the name of the page is what we expect
    assert driver.title == "Україна — Вікіпедія"

    # Find User home page button and emulate a mouse click
    btn3_elem = driver.find_element(By.ID, "pt-userpage")
    btn3_elem.click()

    # Check that the name of the page is what we expect
    assert driver.title == "Привіт, Antonio cassano86! — Вікіпедія"

    # Find User page tab and emulate a mouse click
    btn4_elem = driver.find_element(By.ID, "ca-user")
    btn4_elem.click()

    # Find Talk tab and emulate a mouse click
    btn5_elem = driver.find_element(By.ID, "ca-talk")
    btn5_elem.click()

    # Find "Log out" button and emulate a mouse click
    btn6_elem = driver.find_element(By.ID, "pt-logout")
    btn6_elem.click()

    # Check that the name of the page is what we expect
    assert driver.title == "Вихід із системи — Вікіпедія"

    # Close the browser
    driver.close()
