from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytest

driver = webdriver.Chrome()

def test_login_form():
    driver.get("http://localhost:5000/profil")

    # Metin Girme (send_keys())
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password123")

    # Butona tıklama
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

def test_registration_form():
    driver.get("http://localhost:5000")

    # Metin Girme (send_keys())
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("John")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Doe")

    email = driver.find_element(By.ID, "reg-email")
    email.send_keys("john.doe@example.com")

    password = driver.find_element(By.ID, "reg-password")
    password.send_keys("password123")

    confirm_password = driver.find_element(By.ID, "confirm-password")
    confirm_password.send_keys("password123")

    # Checkbox İşlemleri
    female_checkbox = driver.find_element(By.XPATH, "//input[@name='gender' and @value='Kadın']")
    female_checkbox.click()

    male_checkbox = driver.find_element(By.XPATH, "//input[@name='gender' and @value='Erkek']")
    male_checkbox.click()

    # Radio Button İşlemleri
    animation_radio = driver.find_element(By.XPATH, "//input[@name='animation' and @value='Anime']")
    animation_radio.click()

    # Dropdown Menüsü Yönetme
    preferences_select = Select(driver.find_element(By.ID, "preferences"))
    preferences_select.select_by_visible_text("Aksiyon")

    # Kayıt Ol butonuna tıklama
    register_button = driver.find_element(By.NAME, "register")
    register_button.click()

@pytest.mark.parametrize("email, password", [("test@example.com", "password123")])
def test_login_with_multiple_credentials(email, password):
    driver.get("http://localhost:5000")

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

# Paralel Test Çalıştırma (pytest ile)
if __name__ == "__main__":
    pytest.main(["-n", "2"])  # Paralel olarak 2 test çalıştırılır
