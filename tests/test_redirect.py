import allure
from data import Data
from pages.order_page import OrderPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу "Самоката" при нажатии на логотип "Самокат"')
    def test_go_to_main_page_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_order_button_top()
        order_page.click_on_scooter_logo_button()
        order_page.wait_visibility_of_order_button_down()
        assert order_page.get_current_url() == Data.SCOOTER_URL

    @allure.title('Проверка перехода на страницу "Дзен" через редирект')
    def test_checking_the_transition_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_order_button_top()
        order_page.click_on_yandex_logo_button()
        order_page.switch_to_window(1)
        order_page.wait_visibility_of_find_button()
        assert order_page.get_current_url() == Data.DZEN_URL
