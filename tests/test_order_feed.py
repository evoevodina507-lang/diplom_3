import allure
import pytest
import requests
import time

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


BASE_URL = "https://stellarburgers.education-services.ru/"


@pytest.fixture(scope="function")
def test_user():
    email = f"test_{int(time.time())}@yandex.ru"
    password = "password123"
    name = "TestUser"

    reg_url = BASE_URL + "api/auth/register"

    response = requests.post(
        reg_url,
        json={
            "email": email,
            "password": password,
            "name": name
        }
    )

    assert response.status_code == 200, (
        f"Не удалось создать пользователя: {response.text}"
    )

    yield {
        "email": email,
        "password": password
    }

    login_response = requests.post(
        BASE_URL + "api/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    if login_response.status_code == 200:
        token = login_response.json().get("accessToken")

        if token:
            requests.delete(
                BASE_URL + "api/auth/user",
                headers={"Authorization": token}
            )


@pytest.fixture
def logged_in_user(driver, test_user):
    main_page = MainPage(driver)
    main_page.login_user(
        test_user["email"],
        test_user["password"]
    )
    return main_page


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title(
        "Проверка увеличения счетчика «Выполнено за всё время»"
    )
    def test_total_orders_increases(self, driver, logged_in_user):
        main_page = logged_in_user
        order_feed = OrderFeedPage(driver)

        main_page.click_order_feed()

        initial_count = order_feed.get_total_orders()

        driver.get(BASE_URL)

        main_page.create_order()
        main_page.close_order_modal()

        driver.get(BASE_URL + "feed")

        new_count = order_feed.get_total_orders()

        assert new_count > initial_count

    @allure.title(
        "Проверка увеличения счетчика «Выполнено за сегодня»"
    )
    def test_today_orders_increases(self, driver, logged_in_user):
        main_page = logged_in_user
        order_feed = OrderFeedPage(driver)

        main_page.click_order_feed()

        initial_count = order_feed.get_today_orders()

        driver.get(BASE_URL)

        main_page.create_order()
        main_page.close_order_modal()

        driver.get(BASE_URL + "feed")

        new_count = order_feed.get_today_orders()

        assert new_count > initial_count

    @allure.title(
        "Проверка появления номера заказа в разделе «В работе»"
    )
    def test_order_number_in_progress(self, driver, logged_in_user):
        main_page = logged_in_user

        driver.get(BASE_URL)

        order_number = main_page.create_order()

        main_page.close_order_modal()

        driver.get(BASE_URL + "feed")

        order_feed = OrderFeedPage(driver)

        in_progress_number = order_feed.get_in_progress_order_number()

        assert order_number in in_progress_number