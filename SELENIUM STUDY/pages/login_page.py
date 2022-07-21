from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "not login_url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no login form on the page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'no register form on the page'

    def register_new_user(self, email, password):
        em = self.browser.find_element(By.NAME, 'registration-email')
        em.send_keys(email)
        pass1 = self.browser.find_element(By.NAME, 'registration-password1')
        pass1.send_keys(password)
        pass2 = self.browser.find_element(By.NAME, 'registration-password2')
        pass2.send_keys(password)
        self.browser.find_element(By.NAME, 'registration_submit').click()