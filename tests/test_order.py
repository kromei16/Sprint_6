import allure
import pytest
from data import Data
from pages.order_page import OrderPage

class TestOrder:
    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize(
        ("name", "lastname", "address", "phone", "metro"),
        [("Михаил", "Черный", "ул. Пушкина, д. 55", "89992921144", "Красные ворота"),
        ("Юлия", "Снежкова", "ул. Колотушкина, д. 10", "89992921155", "Речной вокзал")])
    def test_order(self, driver, name, lastname, address, phone, metro):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_next_button()
        order_page.fill_order_form(name, lastname, address, phone, metro)
        order_page.click_on_metro_button()
        order_page.click_on_next_button()
        order_page.wait_visibility_of_date_input()
        order_page.fill_current_date(Data.CURRENT_DATE)
        order_page.click_on_rental_period_button()
        order_page.click_on_one_day_button()
        order_page.click_on_gray_color_button()
        order_page.fill_comment(Data.COMMENT)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        assert order_page.wait_visibility_of_order_placed_text()