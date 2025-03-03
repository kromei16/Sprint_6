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

    @allure.step("Проскролить до FAQ секции»")
    def scroll_to_element_faq(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос №1")
    def click_on_faq_question_button_1(self):
        try:
            # Пытаемся выполнить клик стандартным способом
            self.click_on_element(self.locators.FAQ_QUESTION_1)
        except selenium.common.exceptions.ElementClickInterceptedException:
            # Если возникла ошибка, выполняем клик через JavaScript
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_1)

    @allure.step("Подождать появления ответа на вопрос №1")
    def wait_visibility_of_faq_answer_1(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_1)

    @allure.step("Получить текст ответа на вопрос №1")
    def get_text_of_faq_answer_1(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_1)

    @allure.step("Кликнуть на вопрос №2")
    def click_on_faq_question_button_2(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_2)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_2)

    @allure.step("Подождать появления ответа на вопрос №2")
    def wait_visibility_of_faq_answer_2(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_2)

    @allure.step("Получить текст ответа на вопрос №2")
    def get_text_of_faq_answer_2(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_2)

    @allure.step("Кликнуть на вопрос №3")
    def click_on_faq_question_button_3(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_3)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_3)

    @allure.step("Подождать появления ответа на вопрос №3")
    def wait_visibility_of_faq_answer_3(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_3)

    @allure.step("Получить текст ответа на вопрос №3")
    def get_text_of_faq_answer_3(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_3)

    @allure.step("Кликнуть на вопрос №4")
    def click_on_faq_question_button_4(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_4)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_4)

    @allure.step("Подождать появления ответа на вопрос №4")
    def wait_visibility_of_faq_answer_4(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_4)

    @allure.step("Получить текст ответа на вопрос №4")
    def get_text_of_faq_answer_4(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_4)

    @allure.step("Кликнуть на вопрос №5")
    def click_on_faq_question_button_5(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_5)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_5)

    @allure.step("Подождать появления ответа на вопрос №5")
    def wait_visibility_of_faq_answer_5(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_5)

    @allure.step("Получить текст ответа на вопрос №5")
    def get_text_of_faq_answer_5(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_5)

    @allure.step("Кликнуть на вопрос №6")
    def click_on_faq_question_button_6(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_6)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_6)

    @allure.step("Подождать появления ответа на вопрос №6")
    def wait_visibility_of_faq_answer_6(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_6)

    @allure.step("Получить текст ответа на вопрос №6")
    def get_text_of_faq_answer_6(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_6)

    @allure.step("Кликнуть на вопрос №7")
    def click_on_faq_question_button_7(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_7)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_7)

    @allure.step("Подождать появления ответа на вопрос №7")
    def wait_visibility_of_faq_answer_7(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_7)

    @allure.step("Получить текст ответа на вопрос №7")
    def get_text_of_faq_answer_7(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_7)

    @allure.step("Кликнуть на вопрос №8")
    def click_on_faq_question_button_8(self):
        try:
            self.click_on_element(self.locators.FAQ_QUESTION_8)
        except selenium.common.exceptions.ElementClickInterceptedException:
            self.click_on_element_via_js(self.locators.FAQ_QUESTION_8)

    @allure.step("Подождать появления ответа на вопрос №8")
    def wait_visibility_of_faq_answer_8(self):
        self.wait_visibility_of_element(self.locators.FAQ_ANSWER_8)

    @allure.step("Получить текст ответа на вопрос №8")
    def get_text_of_faq_answer_8(self):
        return self.get_text_of_element(self.locators.FAQ_ANSWER_8)
