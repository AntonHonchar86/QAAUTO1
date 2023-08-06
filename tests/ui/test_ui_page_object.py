from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.ui_wiki import UiWiki
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui1
def test_Wiki_page_object():
    # створення об'єкту сторінки
    ui_wiki = UiWiki()

    # Відкриваємо стартову сторінку Вікіпедії
    ui_wiki.go_to()

    # Виконуємо спробу залогінитись на сайті
    ui_wiki.try_login("Antonio cassano86", ".dtynec86")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert ui_wiki.check_title("Вікіпедія")

    # Виконуємо спробу зробити пошук на сайті
    ui_wiki.try_find_word("Україна")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert ui_wiki.check_title("Україна — Вікіпедія")

    # Перевіряємо можливість зайти на домашню сторінку користувача і там переключатись між вкладками
    ui_wiki.try_in_user_home_page()

    # Перевіряємо можливість вилогінитись з системи
    ui_wiki.try_log_out()

    # Закриваємо браузер
    ui_wiki.close()
