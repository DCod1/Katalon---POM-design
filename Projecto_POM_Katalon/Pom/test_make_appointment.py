import time
from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class Test_course_pack(WebDriverSetup):

    def make_an_appointment(self):
        self.setUp()
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(2)
        home_page.click_make_appoinment()
        time.sleep(2)
        home_page.input_name(driver)
        time.sleep(2)
        home_page.input_password(driver)
        time.sleep(2)
        home_page.click_loggin()
        time.sleep(2)
        home_page.click_select_facility()
        time.sleep(2)
        home_page.click_select_facility_opt3()
        time.sleep(2)
        home_page.click_readmission()
        time.sleep(2)
        home_page.click_healthcare_program()
        time.sleep(2)
        home_page.click_set_date()
        time.sleep(2)
        home_page.click_set_month()
        time.sleep(2)
        home_page.click_set_day()
        time.sleep(2)
        home_page.click_add_comments()
        time.sleep(2)
        home_page.click_book_appointment()
        time.sleep(2)
        home_page.click_go_home()
        time.sleep(5)

        
test= Test_course_pack()

test.make_an_appointment()

