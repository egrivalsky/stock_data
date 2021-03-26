# Stock Bot (Script)
We are going to create a script that retrieves, parses, and store stock data into a MongoDB database

Today, we will be making a script that will be analyzing data from [Wallmine](https://www.wallmine.com)

We need to do a couple of things before we start:
- Set up an account on [Wallmine](https://www.wallmine.com) (it's free)
**IMPORTANT**: Be sure to select ***Sign in with a password*** so you can have that for your *credentials*
- Create a repo if you want to display your work on your personal github or *fork* and *clone* this repo if otherwise
- Create a *.gitignore* file and input the following:
```text
.ipynb_checkpoints
__pycache__/    
credentials.py
```
- Create a *credentials.py* file and store your **email** and **password** from your Wallmine account here
```py
email = "your.email@email.com
password = "yourPassword12345"
```
- Create an *app.py* file add the below code snippet
```py
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
 ```
- Open up Jupyter Lab by using the following command:
```text
jupyter-lab
```
- Create a new notebook (*.ipynb*) file to make code snippets and test

## Resources
- [Selenium Documentation](https://pypi.org/project/selenium/)
- [Selenium Unofficial Docs but Really Good](https://selenium-python.readthedocs.io/index.html)
- [*Lesson: Jupyter Lab - Repo*](https://git.generalassemb.ly/SEIR-111/jupyter_lab)
- [*Lab: LoginBot - Repo*](https://git.generalassemb.ly/SEIR-111/login_bot)
