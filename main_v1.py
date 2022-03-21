from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
from selenium.webdriver.common.by import By
import smtplib

URL = input("Welcome to the warehouse price alerter, please put in the url of something you want to buy\n")
sender_email = YOUR_EMAIL_HERE
sender_password = YOUR_PASSWORD_HERE
user_email = input("Please put in your email for daily alerts\n")


# scrape & parse data
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()))
driver.get(URL)
price = driver.find_element(By.CLASS_NAME, "now-price-integer")
price = int(price.text)
target_price = price/100 * 90

print(f"Thanks, the current price of this product is ${price}")
print("We'll let you know when there's a 10% or more discount")

# email variables
subject = "Instant Price Alert"
new_letter = f"The product price is now below ${target_price}. Buy Now!!"

# sends an email if price is lower than 10%
if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=user_email,
                            msg=f"Subject:{subject}\n\n{new_letter}"
                            )
