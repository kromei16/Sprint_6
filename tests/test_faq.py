import allure
import pytest
from pages.main_page import MainPage

class TestFAQ:
    @allure.title('Проверка раздела «Вопросы о важном» - вопрос №{question_number}')
    @pytest.mark.parametrize("question_number, question_button, answer_locator, expected_answer", [
        (1, 'FAQ_QUESTION_1', 'FAQ_ANSWER_1', "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, 'FAQ_QUESTION_2', 'FAQ_ANSWER_2', "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, 'FAQ_QUESTION_3', 'FAQ_ANSWER_3', "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, 'FAQ_QUESTION_4', 'FAQ_ANSWER_4', "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, 'FAQ_QUESTION_5', 'FAQ_ANSWER_5', "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, 'FAQ_QUESTION_6', 'FAQ_ANSWER_6', "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, 'FAQ_QUESTION_7', 'FAQ_ANSWER_7', "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, 'FAQ_QUESTION_8', 'FAQ_ANSWER_8', "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_question(self, driver, question_number, question_button, answer_locator, expected_answer):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.scroll_to_element_faq()
        getattr(main_page, f'click_on_faq_question_button_{question_number}')()
        main_page.wait_visibility_of_element(getattr(main_page.locators, answer_locator))
        actual_answer = main_page.get_text_of_element(getattr(main_page.locators, answer_locator))
        assert actual_answer == expected_answer, f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"
