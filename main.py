from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def extract_distances(zip_code1, zip_code2):
    # Runs Chrome in a manner to allow for web scraping without being stopped by Cloudflare
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration to improve performance
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox to avoid Chrome hangs
    chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory to avoid Chrome crashes
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    # Enable JavaScript and cookies
    driver.execute_script("navigator.webdriver = false;")
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    # Load the page with Selenium
    base_url = "https://www.freemaptools.com/distance-between-usa-zip-codes.htm"
    driver.get(base_url)

    # Enter zip codes
    zip_input1 = driver.find_element(By.NAME, "pointa")
    zip_input2 = driver.find_element(By.NAME, "pointb")
    zip_input1.send_keys(zip_code1)
    zip_input2.send_keys(zip_code2)

    # Click the 'Show' button
    driver.execute_script("findaandb(document.forms['inp']['pointa'].value,document.forms['inp']['pointb'].value);")

    # Wait for code execution
    time.sleep(5)

    # Wait for the distances to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "distance")))

    # Extract the distances
    distance1 = driver.find_element(By.ID, "distance").get_attribute("value")
    distance2 = driver.find_element(By.ID, "transport").get_attribute("value")

    print("Distance 1 (As the crow flies):", distance1)
    print("Distance 2 (By land transport):", distance2)

    # Close the browser
    driver.quit()

    return distance1, distance2


if __name__ == "__main__":
    zip_code1 = input("Enter first zip code: ")
    zip_code2 = input("Enter second zip code: ")

    distances = extract_distances(zip_code1, zip_code2)
    print("Distances:", distances)
