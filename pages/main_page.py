
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.KRATORNAYA_BUN)

    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_ingredient_counter(self):
        counter = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.KRATORNAYA_BUN_COUNTER
            )
        )
        return int(counter.text.strip())

    def add_ingredient_to_order(self):
        self.drag_and_drop(
            MainPageLocators.KRATORNAYA_BUN,
            MainPageLocators.BASKET_AREA
        )

        self.wait.until(
            lambda driver: self._counter_is_positive()
        )

    def _counter_is_positive(self):
        elements = self.driver.find_elements(
            *MainPageLocators.KRATORNAYA_BUN_COUNTER
        )

        for element in elements:
            if element.is_displayed() and element.text.strip().isdigit():
                if int(element.text.strip()) > 0:
                    return True

        return False

    def is_modal_opened(self):
        try:
            return self.find_element(
                MainPageLocators.MODAL_TITLE
            ).is_displayed()
        except Exception:
            return False

    def login_user(self, email, password):
        from locators.login_page_locators import LoginPageLocators

        self.click_element(MainPageLocators.LOGIN_BUTTON)

        self.find_element(
            LoginPageLocators.EMAIL_INPUT
        ).send_keys(email)

        self.find_element(
            LoginPageLocators.PASSWORD_INPUT
        ).send_keys(password)

        self.click_element(
            LoginPageLocators.LOGIN_SUBMIT_BUTTON
        )

        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON
            )
        )

    def wait_for_order_modal(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL_TITLE
            )
        )

    def get_order_number_from_modal(self):
        number = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL_NUMBER
            )
        )
        return number.text.strip()

    def close_order_modal(self):
        close_button = self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_MODAL_CLOSE
            )
        )

        try:
            close_button.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                close_button
            )

        self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )

    def create_order(self):
        self.add_ingredient_to_order()

        self.click_element(
            MainPageLocators.ORDER_BUTTON
        )

        self.wait_for_order_modal()

        return self.get_order_number_from_modal()
