from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class index:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.title = (By.XPATH, '//span[@data-bind="i18n: settings.$title"]')

    def print_result(self):
        print(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.title)).text)

    def title_assert(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.title)).text
