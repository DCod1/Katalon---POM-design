# import time
# import unittest

from selenium.webdriver.common.by import By


base_url= "https://katalon-demo-cura.herokuapp.com/"



class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.make_appoinment = '//*[@id="btn-make-appointment"]'
        self.name = '//*[@id="login"]/div/div/div[2]/form/div[1]/div[1]/div/div/input'
        self.name_input = '//*[@id="txt-username"]'
        self.password = '//*[@id="login"]/div/div/div[2]/form/div[1]/div[2]/div/div/input'
        self.password_input = '//*[@id="txt-password"]'
        self.loggin = '//*[@id="btn-login"]'
        self.facility = '//*[@id="combo_facility"]'
        self.facility_opt3 = '//*[@id="combo_facility"]/option[3]'
        self.readmission = '//*[@id="appointment"]/div/div/form/div[2]/div/label'
        self.healthcare_program = '//*[@id="appointment"]/div/div/form/div[3]/div/label[2]'
        self.set_date = '//*[@id="txt_visit_date"]'
        self.set_month = '/html/body/div/div[1]/table/thead/tr[2]/th[3]'
        self.set_day = '/html/body/div/div[1]/table/tbody/tr[2]/td[7]'
        self.add_comments = '//*[@id="txt_comment"]'
        self.book_appoinment = '//*[@id="btn-book-appointment"]'
        self.go_home = '//*[@id="summary"]/div/div/div[7]/p/a'

    def get_make_appoinment_search(self):
        return self.driver.find_element(By.XPATH, self.make_appoinment)
      
    def get_loggin_search(self):
        return self.driver.find_element(By.XPATH, self.loggin)
   
    def get_facility_search(self):
        return self.driver.find_element(By.XPATH, self.facility)
    
    def get_facility_opt3_search(self):
        return self.driver.find_element(By.XPATH, self.facility_opt3)
    
    def get_readmission_search(self):
        return self.driver.find_element(By.XPATH, self.readmission)
    
    def get_healthcare_program_search(self):
        return self.driver.find_element(By.XPATH, self.healthcare_program)
    
    def get_set_date_search(self):
        return self.driver.find_element(By.XPATH, self.set_date)
    
    def get_set_month_search(self):
        return self.driver.find_element(By.XPATH, self.set_month)
    
    def get_set_day_search(self):
        return self.driver.find_element(By.XPATH, self.set_day)
    
    def get_add_comments_search(self):
        return self.driver.find_element(By.XPATH, self.add_comments)
    
    def get_book_appoinment_search(self):
        return self.driver.find_element(By.XPATH, self.book_appoinment)
    
    def get_go_home_search(self):
        return self.driver.find_element(By.XPATH, self.go_home)
    

    def click_make_appoinment(self):
        self.get_make_appoinment_search().click()
    
    def input_name(self,driver):
        demo_name_xpath = driver.find_element(By.XPATH, self.name)
        demo_name = demo_name_xpath.get_attribute('value')
        name_input = driver.find_element(By.XPATH, self.name_input)
        name_input.send_keys(demo_name)

    def input_password(self,driver):
        demo_name_xpath = driver.find_element(By.XPATH, self.password)
        demo_name = demo_name_xpath.get_attribute('value')
        name_input = driver.find_element(By.XPATH, self.password_input)
        name_input.send_keys(demo_name)

    def click_loggin(self):
        self.get_loggin_search().click()
 
    def click_select_facility(self):
        self.get_facility_search().click()

    def click_select_facility_opt3(self):
        self.get_facility_opt3_search().click()

    def click_readmission(self):
        self.get_readmission_search().click()

    def click_healthcare_program(self):
        self.get_healthcare_program_search().click()

    def click_set_date(self):
        self.get_set_date_search().click()

    def click_set_month(self):
        self.get_set_month_search().click()
    
    def click_set_day(self):
        self.get_set_day_search().click()
    
    def click_add_comments(self):
        comentario = 'Ing. Diego Fernando Castellanos Vargas'
        self.get_add_comments_search().click()
        comentario_input = self.driver.find_element(By.XPATH,self.add_comments)
        comentario_input.send_keys(comentario)

    def click_book_appointment(self):
        self.get_book_appoinment_search().click()

    def click_go_home(self):
        self.get_go_home_search().click()
        

    @staticmethod
    def get_base_url():
        return base_url