import allure
import selenium
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Кликнуть на кнопку куки «да все привыкли»")
    def click_on_cookie_button(self):
        self.click_on_element(self.locators.COOKIE_BUTTON)

    @allure.step("Проскролить до FAQ секции")
    def scroll_to_element_faq(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос №{question_number}")
    def click_on_faq_question_button(self, question_number):
        locator = self.locators.faq_question_locator(question_number - 1)
        try:
            self.click_on_element(locator)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(locator)

    @allure.step("Подождать появления ответа на вопрос №{question_number}")
    def wait_visibility_of_faq_answer(self, question_number):
        locator = self.locators.faq_answer_locator(question_number - 1)
        self.wait_visibility_of_element(locator)

    @allure.step("Получить текст ответа на вопрос №{question_number}")
    def get_text_of_faq_answer(self, question_number):
        locator = self.locators.faq_answer_locator(question_number - 1)
        return self.get_text_of_element(locator)
