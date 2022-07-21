from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT_LINK = (By.CSS_SELECTOR, 'img[class="thumbnail"]')
    TEXT = (By.ID, 'content_inner')