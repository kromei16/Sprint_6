from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()

    def click_on_element_via_js(self, locator):
        with allure.step(f"Кликнуть на элемент {locator} через JavaScript"):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def wait_visibility_of_element(self, locator):
        with allure.step(f"Подождать видимость элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

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

    def switch_to_window(self, window_index):
        with allure.step(f"Переключиться на окно {window_index}"):
            self.driver.switch_to.window(self.driver.window_handles[window_index])

    def get_current_url(self):
        with allure.step("Получить текущий URL"):
            return self.driver.current_url
