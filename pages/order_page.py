import allure

from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Кликнуть на кнопку куки «Да, все привыкли»")
    def click_on_cookie_button(self):
        cookie_button = self.driver.find_element(*self.locators.COOKIE_BUTTON)
        cookie_button.click()

    @allure.step("Кликнуть на верхнюю кнопку «Заказать»")
    def click_on_order_button_top(self):
        order_button_top = self.driver.find_element(*self.locators.ORDER_BUTTON_TOP)
        order_button_top.click()

    @allure.step("Подождать появления верхней кнопки «Заказать»")
    def wait_visibility_of_order_button_top(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ORDER_BUTTON_TOP)
        )

    @allure.step("Кликнуть на нижнюю кнопку «Заказать»")
    def click_on_order_button_down(self):
        order_button_down = self.driver.find_element(*self.locators.ORDER_BUTTON_DOWN)
        order_button_down.click()

    @allure.step("Подождать появления нижней кнопки «Заказать»")
    def wait_visibility_of_order_button_down(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ORDER_BUTTON_DOWN)
        )

    @allure.step("Кликнуть на логотип «Самокат»")
    def click_on_scooter_logo_button(self):
        scooter_logo_button = self.driver.find_element(*self.locators.SCOOTER_LOGO_BUTTON)
        scooter_logo_button.click()

    @allure.step("Кликнуть на логотип «Яндекс»")
    def click_on_yandex_logo_button(self):
        yandex_logo_button = self.driver.find_element(*self.locators.YANDEX_LOGO_BUTTON)
        yandex_logo_button.click()

    @allure.step("Переключиться на окно {window_index}")
    def switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать появления кнопки «Найти»")
    def wait_visibility_of_find_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.FIND_BUTTON)
        )

    @allure.step("Подождать появления кнопки «Далее»")
    def wait_visibility_of_next_button(self):
        self.wait_visibility_of_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить поля Имя, Фамилия, Адрес, Телефон, Станция метро")
    def fill_order_form(self, name, lastname, address, phone, metro):
        self.fill_input(self.locators.NAME_INPUT, name)
        self.fill_input(self.locators.LASTNAME_INPUT, lastname)
        self.fill_input(self.locators.ADDRESS_INPUT, address)
        self.fill_input(self.locators.PHONE_INPUT, phone)
        self.fill_input(self.locators.METRO_INPUT, metro)

    @allure.step("Выбрать метро из выпадающего списка")
    def click_on_metro_button(self):
        self.click_on_element(self.locators.METRO_BUTTON)

    @allure.step("Кликнуть на кнопку «Далее»")
    def click_on_next_button(self):
        self.click_on_element(self.locators.NEXT_BUTTON)

    @allure.step("Подождать появления поля даты привоза самоката")
    def wait_visibility_of_date_input(self):
        self.wait_visibility_of_element(self.locators.DATE_INPUT)

    @allure.step("Заполнить поле даты привоза самоката")
    def fill_current_date(self, date):
        self.fill_date(self.locators.DATE_INPUT, date)

    @allure.step("Кликнуть на кнопку выбора срока аренды")
    def click_on_rental_period_button(self):
        self.click_on_element(self.locators.RENTAL_PERIOD_BUTTON)

    @allure.step("Выбрать срок аренды «сутки»")
    def click_on_one_day_button(self):
        self.click_on_element(self.locators.ONE_DAY_BUTTON)

    @allure.step("Выбрать цвет самоката «серая безысходность»")
    def click_on_gray_color_button(self):
        self.click_on_element(self.locators.GRAY_COLOR_BUTTON)

    @allure.step("Заполнить поле для комментария")
    def fill_comment(self, text):
        self.fill_input(self.locators.COMMENT_INPUT, text)

    @allure.step("Кликнуть на кнопку «Заказать»")
    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку «Да»")
    def click_on_yes_button(self):
        self.click_on_element(self.locators.YES_BUTTON)

    @allure.step("Подождать появления текста «Заказ оформлен»")
    def wait_visibility_of_order_placed_text(self):
        return self.wait_visibility_of_element(self.locators.ORDER_PLACED_TEXT)
