from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

def send_messages(contact, message, count):
    try:
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.click()
        time.sleep(1)
        search_box.send_keys(contact)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        for i in range(count):
            try:
                message_box = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'))
                )
                message_box.send_keys(message)
                message_box.send_keys(Keys.ENTER)
                time.sleep(0.5)
            except StaleElementReferenceException:
                print("Element is no longer valid. Retrying...")
                continue

        print(f"{count} messages were sent to {contact}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

# (in this case my webdriver is Microsoft Edge)
driver = webdriver.Edge()

driver.get('https://web.whatsapp.com')

print("SCRIPT MADE BY XHALL1! :) \nScan the WhatsApp Web QR code and press Enter.")
input()

contact = input("Enter the name of the contact or group: ")
message = input("Enter the message you want to send: ")

while True:
    try:
        count = int(input("How many times do you want to send the message? "))
        if count <= 0:
            raise ValueError("The count must be a number greater than 0.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

send_messages(contact, message, count)
