from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import json
import time
import zipfile
import shutil

def check_update():
    # Set up download directory
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)
    url = "https://docryptonet.infinityfreeapp.com/app/check_version.php?version=0.9"

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_argument("--headless")  # Optional: run headless

    # Launch Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Wait for download (polling every 0.5 seconds for 5 seconds)
    downloaded_file = None
    for _ in range(10):
        files = os.listdir(download_dir)
        zip_files = [f for f in files if f.endswith(".zip")]
        if zip_files:
            downloaded_file = os.path.join(download_dir, zip_files[0])
            break
        time.sleep(0.5)

    driver.quit()

    if not downloaded_file or not os.path.isfile(downloaded_file):
        print("You have the latest version : 0.9")
        return

    # Extract ZIP and replace or add files to current directory
    with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
        temp_extract_path = os.path.join(download_dir, "temp_extract")
        os.makedirs(temp_extract_path, exist_ok=True)
        zip_ref.extractall(temp_extract_path)

        # Move extracted files/folders to current directory
        for item in os.listdir(temp_extract_path):
            s = os.path.join(temp_extract_path, item)
            d = os.path.join(os.getcwd(), item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

    print("Update completed.")

    # Cleanup
    shutil.rmtree(download_dir)

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

        # Save output to a JSON file
        with open("crypto_info.json", "w") as f:
            json.dump({"crypto_info": plain_output}, f)

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

        # Save output to a JSON file
        with open("add_supply.json", "w") as f:
            json.dump({"add_supply": plain_output}, f)

 finally:
        driver.quit()

def check_balance(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/balance_checker.php"
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

        # Save output to a JSON file
        with open("balance.json", "w") as f:
            json.dump({"balance": plain_output}, f)

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

        # Save output to a JSON file
        with open("wallet_balance.json", "w") as f:
            json.dump({"wallet_balance": plain_output}, f)

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

        # Save output to a JSON file
        with open("locked.json", "w") as f:
            json.dump({"locked": plain_output}, f)

 finally:
        driver.quit()

def check_price(crypto_id):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/price_checker.php"
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

        # Save output to a JSON file
        with open("price.json", "w") as f:
            json.dump({"price": plain_output}, f)

 finally:
        driver.quit()

def remove_supply(crypto_id, amount_remove_supply):
 # URL with query string
 base_url = "https://docryptonet.infinityfreeapp.com/app/remove_supply.php"
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

        # Save output to a JSON file
        with open("removed_supply.json", "w") as f:
            json.dump({"removed_supply": plain_output}, f)

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

        # Save output to a JSON file
        with open("units.json", "w") as f:
            json.dump({"units": plain_output}, f)

    finally:
        driver.quit()

def check_added_supply(crypto_id):
    # URL with query string
    base_url = "https://docryptonet.infinityfreeapp.com/app/check_added_supply.php"
    url = f"{base_url}?crypto_id={crypto_id}"

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

        # Save output to a JSON file
        with open("added_supply.json", "w") as f:
            json.dump({"added_supply": plain_output}, f)

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