import os
import time
import random
import string
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def take_screenshot(url):
    current_time = time.strftime("%H_%M_%S")

    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument(f'--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)

    print(f"[{current_time}] [+] Navigating to {url}")
    try:
        driver.get(url)
    except WebDriverException:
        print(f"[{current_time}] [!] Website Not Found")
        return

    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename = url.split("//")[-1].split("/")[0]
    screenshot_path = os.path.join(output_folder, f'{filename}_{random_string}.png')
    print(f"[{current_time}] [+] Taking Screenshot and saving as {screenshot_path}")
    driver.save_screenshot(screenshot_path)

    print(f"[{current_time}] [+] Closing Browser")
    driver.quit()

def main():
    while True:
        try:
            url = input(f"[{time.strftime('%H:%M:%S')}] [+] Enter Site: ").strip()
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
            take_screenshot(url)
            choice = input(f"[{time.strftime('%H:%M:%S')}] [+] Would you like to Screenshot Another Site (Y/N): ")
            if choice.lower() == 'n':
                break
            elif choice.lower() == 'y':
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(f"[{time.strftime('%H:%M:%S')}] [+] Starting No-Information-Logger (prevent's site from grabbing your information)")
    main()
