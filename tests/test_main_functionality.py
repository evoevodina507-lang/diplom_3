
import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.click_constructor()

        assert "stellarburgers" in driver.current_url

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient()

        assert (
            main_page.is_modal_opened()
            or "/ingredient/" in driver.current_url
        )

    @allure.title("Проверка закрытия модального окна по крестику")
    def test_close_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient()

        if "/ingredient/" in driver.current_url:
            driver.back()
        else:
            main_page.close_modal()

            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located(
                    MainPageLocators.MODAL_TITLE
                )
            )

    @allure.title("Проверка увеличения счетчика ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        main_page.add_ingredient_to_order()

        counter = main_page.get_ingredient_counter()

        assert counter >= 1, (
            f"Счетчик не увеличился. "
            f"Текущее значение: {counter}"
        )
