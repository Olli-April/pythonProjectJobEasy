from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='/Users/olgalonchuk/PycharmProjects/pythonProjectJobEasy/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/')

    def test_best(self):
        self.driver.find_elements(By.XPATH, "//div[@id='nav-xshop']/a[contains(@href,'bestseller')]").click()
        actual_links = self.driver.find_elements(By.XPATH, "//div[@id='zg_tabs']//li")
        assert len(actual_links) == 5, f"Expected to see 5 bestseller links, but'got '{len(actual_links)}'"

    def teardown_method(self):
        self.driver.quit()
