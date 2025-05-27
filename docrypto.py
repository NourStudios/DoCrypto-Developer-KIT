from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def create_crypto(name, shortname, username, password):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/create_crypto.php"
 url = f"{base_url}?name={name}&short={shortname}&username={username}&password={password}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def add_supply(crypto_id, amount_add_supply):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/add_supply.php"
 url = f"{base_url}?crypto={crypto_id}&amount={amount_add_supply}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def run_algorithm(crypto_id, amount_algorithm, owner_pct):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/algorithm.php"
 url = f"{base_url}?crypto={crypto_id}&amount={amount_algorithm}&owner_pct={owner_pct}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def check_balance(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/balance_checker.php"
 url = f"{base_url}?crypto={crypto_id}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def check_wallet_balance(public_address, wallet_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/check_wallet.php"
 url = f"{base_url}?crypto_address={public_address}&username={wallet_id}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def lock_crypto(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/locked_crypto.php"
 url = f"{base_url}?cryptoid={crypto_id}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def check_price(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/add_supply.php"
 url = f"{base_url}?cryptoid={crypto_id}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def remove_supply(crypto_id, amount_remove_supply):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/add_supply.php"
 url = f"{base_url}?crypto={crypto_id}&amount={amount_remove_supply}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

def check_units(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/units_checker.php"
 url = f"{base_url}?cryptoid={crypto_id}"
 # Chrome options
 options = Options()
 options.add_argument("--headless")
 options.add_argument("--disable-gpu")
 options.add_argument("--log-level=3")  # Suppress console logs

 # Suppress "DevTools listening" by redirecting service logs
 service = Service(log_path=os.devnull)

 # Start WebDriver
 driver = webdriver.Chrome(service=service, options=options)

 try:
     driver.get(url)
     plain_output = driver.find_element("tag name", "body").text
     print(plain_output)
 finally:
     driver.quit()

name = ""
shortname = ""
username = ""
password = ""
crypto_id = ""
amount_add_supply = ""
amount_remove_supply = ""
amount_algorithm = ""
owner_pct =""
wallet_username = ""
public_address = ""
wallet_id = ""
