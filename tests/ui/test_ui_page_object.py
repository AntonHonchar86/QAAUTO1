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


# Individual tests


@pytest.mark.ui_my
def test_Wiki_page_object():
    # Create a page object
    ui_wiki = UiWiki()

    # Open the Wikipedia page
    ui_wiki.go_to()

    # Check that the name of the page is what we expect
    assert ui_wiki.check_title("Вікіпедія")

    # Try to Log in
    ui_wiki.try_login("Antonio cassano86", ".dtynec86")

    # Check that the name of the page is what we expect
    assert ui_wiki.check_title("Вікіпедія")

    # Trying to search on the site
    ui_wiki.try_find_word("Україна")

    # Check that the name of the page is what we expect
    assert ui_wiki.check_title("Україна — Вікіпедія")

    # Check the ability to enter to the User home page and switch between tabs
    ui_wiki.try_in_user_home_page()

    # Try to Log out
    ui_wiki.try_log_out()

    # Check that the name of the page is what we expect
    assert ui_wiki.check_title("Вихід із системи — Вікіпедія")

    # Close the browser
    ui_wiki.close()
