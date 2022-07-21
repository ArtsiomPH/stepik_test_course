from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def save_product_name(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return prod_name

    def save_product_price(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return prod_price

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE)

    def should_be_product_name_in_msg(self):
        message_text = self.browser.find_element(*ProductPageLocators.MESSAGE).text
        assert self.save_product_name() == message_text

    def should_be_product_price_equal_cart_price(self):
        price_message_text = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert self.save_product_price() in price_message_text