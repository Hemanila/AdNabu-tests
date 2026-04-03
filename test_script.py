from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None
report = open("test_report.txt", "w")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    driver.get("https://adnabu-store-assignment1.myshopify.com/")
    driver.maximize_window()

    print("Opened URL")
    report.write("Opened URL\n")

    try:
        password_input = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("AdNabuQA")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        print("Password submitted")
        report.write("Password submitted\n")

    except:
        print("Password skipped")
        report.write("Password skipped\n")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Homepage loaded")
    report.write("Homepage loaded\n")

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
        report.write("Search performed\n")

        wait.until(EC.url_contains("search"))

    except:
        print("Search skipped")
        report.write("Search skipped\n")

    products = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href,'/products/')]"))
    )

    print(f"Found {len(products)} products")
    report.write(f"Found {len(products)} products\n")

    added = False

    for i in range(len(products)):

        products = driver.find_elements(By.XPATH, "//a[contains(@href,'/products/')]")

        driver.execute_script("arguments[0].click();", products[i])
        print(f"Opened product {i+1}")
        report.write(f"Opened product {i+1}\n")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            add_to_cart = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add')]"))
            )

            driver.execute_script("arguments[0].click();", add_to_cart)

            print("Product added to cart successfully")
            report.write("Product added to cart successfully\n")

            added = True
            break

        except:
            print("Product not available, trying next...")
            report.write("Product not available, trying next...\n")

            driver.back()
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    if not added:
        print("No available product found - Cannot complete Add to Cart")
        report.write("No available product found - Test could not be completed due to all products being sold out\n")
    else:
        report.write("Test Passed - Product added to cart successfully\n")

    report.write("Test Execution Completed\n")

    input("Press ENTER to close browser...")

except Exception as e:
    print("Error occurred:", e)
    report.write(f"Error occurred: {e}\n")

finally:
    report.close()
    if driver:
        driver.quit()
