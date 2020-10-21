from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAmazon:

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='/Users/olgalonchuk/PycharmProjects/pythonProjectJobEasy/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/')

    def test_empty_cart(self):
        self.driver.find_element(By.ID,'nav-cart').click()
        actual_text = self.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
        expected_text = "Your Amazon Cart is empty"
        assert actual_text == expected_text, f"Error. Expected text: '{expected_text}', but actual text '{actual_text}'"



    def teardown_method(self):
        self.driver.quit()
