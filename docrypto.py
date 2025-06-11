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
    url = "http://dobnet.infinityfreeapp.com/check_version.php?version=1.2"

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
        print("You have the latest version : 1.2")
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

def create_crypto(name, shortname, format_type, format_length):
 # URL with query string
 base_url = "http://dobnet.infinityfreeapp.com/create_b.php"
 url = f"{base_url}?name={name}&short={shortname}&format_type={format_type}&format_length={format_length}"
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

def add_supply(crypto_id, amount_add_supply, crypto_password):
 # URL with query string
 base_url = "http://dobnet.infinityfreeapp.com/add_supply.php"
 url = f"{base_url}?b={crypto_id}&amount={amount_add_supply}&password={crypto_password}"
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

def check_balance(crypto_id, crypto_password):
 # URL with query string
 base_url = "http://dobnet.infinityfreeapp.com/check_balance.php"
 url = f"{base_url}?bid={crypto_id}&password={crypto_password}"
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

def check_price(public_address):
 # URL with query string
 base_url = "http://dobnet.infinityfreeapp.com/check_price.php"
 url = f"{base_url}?public_address={public_address}"
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

def remove_supply(crypto_id, amount_remove_supply, crypto_password):
 # URL with query string
 base_url = "http://dobnet.infinityfreeapp.com/remove_supply.php"
 url = f"{base_url}?b={crypto_id}&amount={amount_remove_supply}&password={crypto_password}"
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

def check_units(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_supply.php"
    url = f"{base_url}?bid={crypto_id}&password={crypto_password}"

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

def check_added_supply(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_added_supply.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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

def check_attraction(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_attraction.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("attraction.json", "w") as f:
            json.dump({"attraction": plain_output}, f)

    finally:
        driver.quit()

def check_transactions(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_a.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("transactions.json", "w") as f:
            json.dump({"transactions": plain_output}, f)

    finally:
        driver.quit()

def check_buy_orders(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_buy_requests.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("buy_orders.json", "w") as f:
            json.dump({"orders": plain_output}, f)

    finally:
        driver.quit()

def check_crypto(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_b.php"
    url = f"{base_url}?bid={crypto_id}&password={crypto_password}"

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
        with open("check_crypto.json", "w") as f:
            json.dump({"crypto": plain_output}, f)

    finally:
        driver.quit()

def check_wallet(public_address, wallet_username, wallet_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_wallet.php"
    url = f"{base_url}?b_address={public_address}&username={wallet_username}&password={wallet_password}"

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
            json.dump({"balance": plain_output}, f)

    finally:
        driver.quit()

def set_market(crypto_id, set_buy_sell, users, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/set_market.php"
    url = f"{base_url}?b_id={crypto_id}&market_action={set_buy_sell}&userParam={users}&password={crypto_password}"

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
        with open("set_market.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def set_sell_fees(crypto_id, fees, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/set_sell_fees.php"
    url = f"{base_url}?id={crypto_id}&fee={fees}&password={crypto_password}"

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
        with open("set_sell_fees.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def set_buy_fees(crypto_id, fees, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/set_buy_fees.php"
    url = f"{base_url}?b={crypto_id}&fee={fees}&password={crypto_password}"

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
        with open("set_sell_fees.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def show_wallets(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/show_wallets.php"
    url = f"{base_url}?id={crypto_id}&password={crypto_password}"

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
        with open("show_wallets.json", "w") as f:
            json.dump({"wallets": plain_output}, f)

    finally:
        driver.quit()

def transfer(crypto_id, amount_transfer, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/transfer.php"
    url = f"{base_url}?b_id={crypto_id}&amount={amount_transfer}&password={crypto_password}"

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
        with open("transfer.json", "w") as f:
            json.dump({"transfer": plain_output}, f)

    finally:
        driver.quit()

def check_sell_orders(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_sell_requests.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("sell_orders.json", "w") as f:
            json.dump({"orders": plain_output}, f)

    finally:
        driver.quit()

def buy_coins(public_address, wallet_username, wallet_password, buy_coins_amount, username, user_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/buy_sell.php"
    url = f"{base_url}?public_address={public_address}&wallet_username={wallet_username}&wallet_password={wallet_password}&action=buy&amount={buy_coins_amount}&username={username}&password={user_password}"

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
        with open("buy_coins.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def sell_coins(public_address, wallet_username, wallet_password, buy_coins_amount, username, user_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/buy_sell.php"
    url = f"{base_url}?public_address={public_address}&wallet_username={wallet_username}&wallet_password={wallet_password}&action=sell&amount={buy_coins_amount}&username={username}&password={user_password}"

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
        with open("sell_coins.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def transfer_balance_fees(crypto_id, balance_fees_amount, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/transfer_balance_fees.php"
    url = f"{base_url}?b_id={crypto_id}&amount={balance_fees_amount}&password={crypto_password}"

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
        with open("transfer_balance_fees.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def check_balance_fees(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_balance_fees.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("check_balance_fees.json", "w") as f:
            json.dump({"balance_fees": plain_output}, f)

    finally:
        driver.quit()

def check_sell_prices(public_address):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_sell_prices.php"
    url = f"{base_url}?public_address={public_address}"

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
        with open("check_sell_prices.json", "w") as f:
            json.dump({"sell_prices": plain_output}, f)

    finally:
        driver.quit()

def check_wallet_transactions(crypto_id, wallet_username, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/get_b_transaction_amounts.php"
    url = f"{base_url}?b_id={crypto_id}&wallet_username={wallet_username}&password={crypto_password}"

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
        with open("check_wallet_transactions.json", "w") as f:
            json.dump({"wallet_transactions": plain_output}, f)

    finally:
        driver.quit()

def solve_nodes(miner_username, miner_password, wallet_username):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/SMinerService.php"
    url = f"{base_url}?miner_username={miner_username}&miner_password={miner_password}&wallet_username={wallet_username}"

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
        with open("solve_nodes.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def t_service_solve_nodes(miner_username, miner_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/TSMinerService.php"
    url = f"{base_url}?miner_username={miner_username}&miner_password={miner_password}"

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
        with open("t_solve_nodes.json", "w") as f:
            json.dump({"solve_nodes": plain_output}, f)

    finally:
        driver.quit()

def generate_miner_integeration_certificate(crypto_id, crypto_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/GenerateMinerIntegerationCertificate.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}"

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
        with open("miner_certificate.json", "w") as f:
            json.dump({"miner_credentials": plain_output}, f)

    finally:
        driver.quit()

def order_buy(username, user_password, p2p_buy_amount_coins, public_address, wallet_username):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/order_buy.php"
    url = f"{base_url}?username={username}&password={user_password}&amount={p2p_buy_amount_coins}&public_address={public_address}&wallet_username={wallet_username}"

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
        with open("order_buy.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def order_sell(wallet_username, p2p_sell_amount_coins, public_address, wallet_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/order_sell.php"
    url = f"{base_url}?wallet_username={wallet_username}&wallet_password={wallet_password}&amount={p2p_sell_amount_coins}&public_address={public_address}"

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
        with open("order_sell.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def stake_process(wallet_username, p2p_sell_amount_coins, public_address, wallet_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/order_sell.php"
    url = f"{base_url}?wallet_username={wallet_username}&wallet_password={wallet_password}&amount={p2p_sell_amount_coins}&public_address={public_address}&wallet_username={wallet_username}&stake=true"

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
        with open("stake_process.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def finish_stake(wallet_username, wallet_password, public_address):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/finish_stake.php"
    url = f"{base_url}?wallet_username={wallet_username}&wallet_password={wallet_password}&public_address={public_address}"

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
        with open("finish_stake.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def set_apy(crypto_id, crypto_password, apy_amount, duration, stake_limit):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/set_apy.php"
    url = f"{base_url}?b_id={crypto_id}&password={crypto_password}&apy={apy_amount}&days={duration}&stake_max={stake_limit}"

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
        with open("set_apy.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def set_stake(wallet_username, amount_coins, public_address, wallet_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/set_stake.php"
    url = f"{base_url}?wallet_username={wallet_username}&wallet_password={wallet_password}&amount={amount_coins}&public_address={public_address}"

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
        with open("set_stake.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()

def check_user_balance(username, user_password):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/check_user.php"
    url = f"{base_url}?username={username}&password={user_password}"

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
        with open("user_balance.json", "w") as f:
            json.dump({"balance": plain_output}, f)

    finally:
        driver.quit()

def create_wallet(public_address):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/create_wallet.php"
    url = f"{base_url}?public_address={public_address}"

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
        with open("wallet_credentials.json", "w") as f:
            json.dump({"credentials": plain_output}, f)

    finally:
        driver.quit()

def create_account(username, user_password, email):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/register.php"
    url = f"{base_url}?username={username}&email={email}&password={user_password}"

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
        with open("account_credentials.json", "w") as f:
            json.dump({"credentials": plain_output}, f)

    finally:
        driver.quit()

def send_coins(wallet_username, wallet_reciever, send_coins_amount, wallet_password, public_address):
    # URL with query string
    base_url = "http://dobnet.infinityfreeapp.com/send_recieve.php"
    url = f"{base_url}?from={wallet_username}&to={wallet_reciever}&amount={send_coins_amount}&password={wallet_password}&public_address={public_address}"

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
        with open("send_coins.json", "w") as f:
            json.dump({"status": plain_output}, f)

    finally:
        driver.quit()