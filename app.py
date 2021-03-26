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
     self.driver = webdriver.Chrome('/Users/romebell/downloads/chromedriver-4') # use your path to your Chromedriver
  
  def login(self):
    '''Method used to login into Wallmine account'''
  
    
  def retrieve_data(self):
    '''Method use to retrieve stock data from Wallmine'''
  
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