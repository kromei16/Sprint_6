from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def faq_question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer_locator(index):
        return By.ID, f"accordion__panel-{index}"
