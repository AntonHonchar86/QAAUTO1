from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class UiWiki(BasePage):
    URL = "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(UiWiki.URL)

    def try_login(self, username, password):
        # Знаходимо кнопку Увійти і емулюємо клік мишкою
        btn_elem = self.driver.find_element(By.ID, "pt-login")
        btn_elem.click()

        # Знаходимо поле для логіну користувача і вводимо логін користувача
        user_elem = self.driver.find_element(By.ID, "wpName1")
        user_elem.send_keys(username)

        # Знаходимо поле для паролю і вводимо пароль
        pass_elem = self.driver.find_element(By.ID, "wpPassword1")
        pass_elem.send_keys(password)

        # Знаходимо кнопку Вхід і емулюємо клік мишкою
        btn1_elem = self.driver.find_element(By.NAME, "wploginattempt")
        btn1_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def try_find_word(self, word):
        # Знаходимо поле для пошуку і вводимо слово для пошуку
        search_elem = self.driver.find_element(By.NAME, "search")
        search_elem.send_keys(word)

        # Знаходимо кнопку Пошук і емулюємо клік мишкою
        btn2_elem = self.driver.find_element(By.ID, "searchButton")
        btn2_elem.click()

    def try_in_user_home_page(self):
        # Знаходимо кнопку домашньої сторінки користувача і емулюємо клік мишкою
        btn3_elem = self.driver.find_element(By.ID, "pt-userpage")
        btn3_elem.click()

        # Знаходимо вкладку сторінки користувача і емулюємо клік мишкою
        btn4_elem = self.driver.find_element(By.ID, "ca-user")
        btn4_elem.click()

        # Знаходимо кнопку обговорення і емулюємо клік мишкою
        btn5_elem = self.driver.find_element(By.ID, "ca-talk")
        btn5_elem.click()

    def try_log_out(self):
        # Знаходимо кнопку Вийти і емулюємо клік мишкою
        btn6_elem = self.driver.find_element(By.ID, "pt-logout")
        btn6_elem.click()
