
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    driver.get("https://adnabu-store-assignment1.myshopify.com/")
    driver.maximize_window()

    print("Opened URL")

    try:
        password_input = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("AdNabuQA")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        print("Password submitted")

    except:
        print("Password skipped")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Homepage loaded")

    try:
        search_icon = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(@class,'search')]"))
        )
        search_icon.click()

        search_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))
        )

        search_box.send_keys("Shoes")
        search_box.send_keys(Keys.RETURN)

        print("Search performed")
        wait.until(EC.url_contains("search"))

    except:
        print("Search skipped")

    products = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href,'/products/')]"))
    )

    print(f"Found {len(products)} products")

    for i in range(len(products)):

        products = driver.find_elements(By.XPATH, "//a[contains(@href,'/products/')]")
        driver.execute_script("arguments[0].click();", products[i])

        print(f"Opened product {i+1}")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            add_to_cart = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add')]"))
            )

            driver.execute_script("arguments[0].click();", add_to_cart)

            print("Product added to cart successfully")
            break

        except:
            print("Product not available, trying next...")
            driver.back()
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    input("Press ENTER to close browser...")

except Exception as e:
    print("Error occurred:", e)

finally:
    if driver:
        driver.quit()
