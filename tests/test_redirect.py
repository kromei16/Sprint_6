import allure
from data import Data
from pages.order_page import OrderPage


class TestRedirect:
    @allure.title('Проверка переходов по сайту и редиректа на страницу Yandex')
    def test_yandex_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_button()
        order_page.click_on_order_button_top()
        order_page.wait_visibility_of_next_button()
        order_page.click_on_scooter_logo_button()
        order_page.wait_visibility_of_order_button_down()
        order_page.click_on_order_button_down()
        order_page.wait_visibility_of_next_button()
        order_page.click_on_yandex_logo_button()
        driver.switch_to.window(driver.window_handles[1])
        order_page.wait_visibility_of_find_button()
        assert driver.current_url == Data.DZEN_URL
