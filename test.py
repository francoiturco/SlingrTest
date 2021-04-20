import unittest
from selenium import webdriver
from pageObject.loginPage import login
from pageObject.indexPage import index
import time
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
        option = Options()
        #option.add_argument('start-maximized')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('./SlingrTest/driver/chromedriver.exe', chrome_options=option)
        self.driver.get('https://simpletaskmanager.slingrs.io/dev/runtime/login.html')
        self.driver.implicitly_wait(20)
        self.login = login(self.driver)
        self.index = index(self.driver)

    def test_1_login(self):
        self.login.send_user_name('francoiturco@gmail.com')
        self.login.send_password('wYVRTcMmku3UtjH')
        self.login.click_login()
        self.index.print_result()
        self.assertTrue(self.index.title_assert() == 'SIMPLE TASK MANAGER')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()