import allure
import pytest
from pages.main_page import MainPage
from data import FAQData

class TestFAQ:
    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №{question_number}')
    @pytest.mark.parametrize("question_number, expected_answer", FAQData.QUESTIONS_AND_ANSWERS)
    def test_question(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.scroll_to_element_faq()
        main_page.click_on_faq_question_button(question_number)
        actual_answer = main_page.get_text_of_faq_answer(question_number)
        assert actual_answer == expected_answer, f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"
