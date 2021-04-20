from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class login:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.user_and_password = (By.XPATH, '//input[@class="form-control fullWidth"]')
        self.login_button = (By.XPATH, '//span[contains(text(),"Login")]')

    def send_user_name(self, user):
        self.driver.find_elements(*self.user_and_password)[0].send_keys(user)

    def send_password(self, password):
        self.driver.find_elements(*self.user_and_password)[1].send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.login_button)).click()