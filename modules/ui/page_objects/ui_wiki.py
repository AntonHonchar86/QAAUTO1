from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class UiWiki(BasePage):
    URL = "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(UiWiki.URL)

    def try_login(self, username, password):
        # Find "Log In" button and emulate a mouse click
        btn_elem = self.driver.find_element(By.ID, "pt-login")
        btn_elem.click()

        # Find field for Username and enter Username
        user_elem = self.driver.find_element(By.ID, "wpName1")
        user_elem.send_keys(username)

        # Find field for Password and enter Password
        pass_elem = self.driver.find_element(By.ID, "wpPassword1")
        pass_elem.send_keys(password)

        # Find "Log in" button and emulate a mouse click
        btn1_elem = self.driver.find_element(By.NAME, "wploginattempt")
        btn1_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def try_find_word(self, word):
        # Find search field and enter Search word
        search_elem = self.driver.find_element(By.NAME, "search")
        search_elem.send_keys(word)

        # Find Search button and emulate a mouse click
        btn2_elem = self.driver.find_element(By.ID, "searchButton")
        btn2_elem.click()

    def try_in_user_home_page(self):
        # Find User home page button and emulate a mouse click
        btn3_elem = self.driver.find_element(By.ID, "pt-userpage")
        btn3_elem.click()

        # Find User page tab and emulate a mouse click
        btn4_elem = self.driver.find_element(By.ID, "ca-user")
        btn4_elem.click()

        # Find Talk tab and emulate a mouse click
        btn5_elem = self.driver.find_element(By.ID, "ca-talk")
        btn5_elem.click()

    def try_log_out(self):
        # Find "Log out" button and emulate a mouse click
        btn6_elem = self.driver.find_element(By.ID, "pt-logout")
        btn6_elem.click()
