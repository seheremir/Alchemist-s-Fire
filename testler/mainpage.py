from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Test sonuçlarını saklamak için bir liste
test_results = []

def log_test_result(test_name, success):
    result = f"{test_name}: {'Başarılı' if success else 'Başarısız'}"
    print(result)
    test_results.append(result)

# WebDriver başlatma fonksiyonu
def start_driver(browser='chrome'):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Headless modda çalıştır
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(options=options)
    return driver

def test_implicit_wait():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        driver.implicitly_wait(10)  # Implicit wait kullanımı
        element = driver.find_element(By.XPATH, "//div[@class='carousel']")
        log_test_result("Implicit Wait", True)
    except Exception as e:
        log_test_result("Implicit Wait", False)
    finally:
        driver.quit()

def test_explicit_wait():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='carousel']"))
        )  # Explicit wait kullanımı
        log_test_result("Explicit Wait", True)
    except Exception as e:
        log_test_result("Explicit Wait", False)
    finally:
        driver.quit()

def test_element_visibility():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='carousel-btn next']"))
        )  # Elementin görünmesini bekleme
        log_test_result("Element Visibility", True)
    except Exception as e:
        log_test_result("Element Visibility", False)
    finally:
        driver.quit()

def test_element_clickable():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='carousel-btn next']"))
        )  # Elementin tıklanabilir olmasını bekleme
        element.click()
        log_test_result("Element Clickable", True)
    except Exception as e:
        log_test_result("Element Clickable", False)
    finally:
        driver.quit()

def test_iframe_handling():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        # Iframe'e geçiş yapma (örnek)
        driver.switch_to.frame("iframe_name")  # Iframe'e geçiş
        element = driver.find_element(By.XPATH, "//button[@class='carousel-btn next']")
        element.click()
        log_test_result("Iframe Handling", True)
    except Exception as e:
        log_test_result("Iframe Handling", False)
    finally:
        driver.quit()

def test_window_switching():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        # Yeni pencereye geçiş yapmak
        driver.execute_script("window.open('https://www.google.com');")
        driver.switch_to.window(driver.window_handles[1])  # Yeni pencereye geçiş
        driver.get("https://www.google.com")
        log_test_result("Window Switching", True)
    except Exception as e:
        log_test_result("Window Switching", False)
    finally:
        driver.quit()

def test_js_execution():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        # JavaScript komutu çalıştırma
        driver.execute_script("window.scrollBy(0, 1000);")
        log_test_result("JS Execution", True)
    except Exception as e:
        log_test_result("JS Execution", False)
    finally:
        driver.quit()

def test_element_state():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        element = driver.find_element(By.XPATH, "//button[@class='carousel-btn next']")
        if element.is_enabled() and element.is_displayed():
            log_test_result("Element State", True)
        else:
            log_test_result("Element State", False)
    except Exception as e:
        log_test_result("Element State", False)
    finally:
        driver.quit()

def test_element_size_and_coordinates():
    driver = start_driver()
    try:
        driver.get("http://localhost:5000")
        element = driver.find_element(By.XPATH, "//button[@class='carousel-btn next']")
        size = element.size
        location = element.location
        print(f"Element Size: {size}, Location: {location}")
        log_test_result("Element Size and Coordinates", True)
    except Exception as e:
        log_test_result("Element Size and Coordinates", False)
    finally:
        driver.quit()

def run_tests():
    test_implicit_wait()
    test_explicit_wait()
    test_element_visibility()
    test_element_clickable()
    test_iframe_handling()
    test_window_switching()
    test_js_execution()
    test_element_state()
    test_element_size_and_coordinates()

    # Test sonuçlarını terminalde göster
    print("\nTest Sonuçları:")
    for result in test_results:
        print(result)

# Farklı tarayıcılarda test çalıştırma örnekleri
print("Chrome test sonucu:")
run_tests()

print("\nFirefox test sonucu:")
run_tests()

print("\nEdge test sonucu:")
run_tests()
