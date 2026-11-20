from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(
            EC.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            EC.visibility_of_element_located(target_locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            source
        )

        ActionChains(self.driver) \
            .move_to_element(source) \
            .click_and_hold() \
            .pause(0.5) \
            .move_to_element(target) \
            .pause(0.5) \
            .release() \
            .perform()