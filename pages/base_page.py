from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        with allure.step('Проскролить до элемента'):
            element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def click_on_element(self, locator):
        with allure.step(f"Кликнуть на элемент {locator}"):
            # Подождать, пока элемент станет кликабельным
            element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
            element.click()

    def click_on_element_via_js(self, locator):
        with allure.step(f"Кликнуть на элемент {locator} через JavaScript"):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def wait_visibility_of_element(self, locator):
        with allure.step(f"Подождать видимость элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def get_text_of_element(self, locator):
        with allure.step(f"Получить текст элемента {locator}"):
            return self.driver.find_element(*locator).text

    def fill_input(self, locator, text):
        with allure.step(f"Заполнить поле {locator}"):
            self.driver.find_element(*locator).send_keys(text)

    def fill_date(self, locator, date):
        with allure.step("Заполнить дату"):
            self.driver.find_element(*locator).send_keys(date)
            self.driver.find_element(*locator).send_keys(Keys.RETURN)
