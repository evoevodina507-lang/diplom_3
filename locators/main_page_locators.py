
from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (
        By.XPATH, "//p[text()='Конструктор']"
    )

    ORDER_FEED_BUTTON = (
        By.XPATH, "//p[text()='Лента Заказов']"
    )

    KRATORNAYA_BUN = (
        By.XPATH, "//img[@alt='Краторная булка N-200i']"
    )

    KRATORNAYA_BUN_COUNTER = (
        By.XPATH,
        "//img[@alt='Краторная булка N-200i']"
        "/ancestor::*[contains(@class, 'BurgerIngredient_ingredient')][1]"
        "//*[contains(@class, 'counter_counter__num')]"
    )

    BASKET_AREA = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]"
    )

    MODAL_TITLE = (
        By.XPATH, "//h2[text()='Детали ингредиента']"
    )

    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    ORDER_MODAL_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'идентификатор заказа')]"
    )

    # Номер заказа находится в h2, а не в p
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large')]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__container')]"
    )

    ORDER_MODAL_CLOSE = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    LOGIN_BUTTON = (
        By.XPATH, "//button[text()='Войти в аккаунт']"
    )
