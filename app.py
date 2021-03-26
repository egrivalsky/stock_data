from selenium import webdriver
import datetime, re, requests, io, time, random, string
from bs4 import BeautifulSoup
from credentials import email, password
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

class StockData:
      def __init__(self):
     '''Initialize an instance of StockData'''
     self.raw_data = []
     self.data = []
     self.urls = {
      'sign_in': 'https://wallmine.com/users/sign-in',
      'homepage': 'https://wallmine.com/',
      'view_stock': lambda exchange, symbol: f'https://wallmine.com/{exchange}/{symbol}'
     }
     self.driver = webdriver.Chrome(r"C:\Users\Erik\Downloads\chromedriver.exe") # use your path to your Chromedriver
  
def login():
    '''Method used to login into Wallmine account'''
    self.driver.get(urls['sign_in'])
    time.sleep(3)
    self.driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/div[1]/div[2]/a').click()
    time.sleep(0.5)
    self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(email)
    self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
    time.sleep(0.1)
    self.driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/div[2]/div[1]/button').click()
    time.sleep(3)
    if self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[1]/h1/span'):
        print('Login was successful')
  
    
    def retrieve_data(self):
        '''Method use to retrieve stock data from Wallmine'''
        # We need to be on the site after login in order for this method to work
    #     self.driver.find_element_by_xpath('/html/body/main/section/div[3]/div[2]/div[1]/div[3]/div/div/a').click()
        self.driver.get('https://wallmine.com/screener?e%5B%5D=NYSE&e%5B%5D=NASDAQ&e%5B%5D=NYSEMKT&hm=performance_today_with_ah&r=m')
        time.sleep(5)
        text = self.driver.find_element_by_xpath('/html/body/main/section/div[4]/div/div/div[1]/div/div[1]/h1').text
        if text == 'Free Stock Screener':
            print('On the right page')
    #     self.driver.find_element_by_xpath('/html/body/main/section/div[5]/form/div/div').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath('/html/body/main/section/div[5]/div/div/div[1]/div/ul/li[1]/a').click() # click on overview tab
        self.driver.get('https://wallmine.com/screener?e%5B%5D=NASDAQ&e%5B%5D=NYSE&e%5B%5D=NYSEMKT&r=o&o=m&d=d&hm=performance_today_with_ah&fo=e%5B%5D')
        time.sleep(2)
        table_head = self.driver.find_element_by_xpath('/html/body/main/section/div[5]/div/div/div[2]/table/thead').text
        table_body = self.driver.find_element_by_xpath('/html/body/main/section/div[5]/div/div/div[2]/table/tbody').text
        raw_data = [table_head, table_body]
        return raw_data
  
  def parse_data(self):
    '''Method used to parse the data that was retrieved'''
  
  def store_data(self): 
    '''Method used to store the data inside a MongoDB database'''
  
  def view_stock(self, ticker): 
    '''Method used to view a stock'''
    # View the webpage and return a string of the stock info
  
  def compare_price(self, exchange, symbol): 
    '''Method used to compare the current price of a stock to the price in the database'''
    # Return an object with the realtime price and price in database
    
  def stop_program(self):
    '''Method used to close the program'''
    print('Closing program in 5 seconds...')
    time.sleep(5)
    self.driver.close()
    
    