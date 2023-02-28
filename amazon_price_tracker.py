# importing libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://www.amazon.com/Morningwood-Offensive-Novelty-Graphic-Tees/dp/B00PJARZ7M/ref=sxin_16_pa_sp_search_thematic_sspa?c=ts&content-id=amzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab%3Aamzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab&cv_ct_cx=Novelty+Clothing+%26+More&keywords=Novelty+Clothing+%26+More&pd_rd_i=B00PJARZ7M&pd_rd_r=e972c888-7136-4bf3-80c6-2619b50f523d&pd_rd_w=Kyrm2&pd_rd_wg=E81dI&pf_rd_p=948775b6-578a-48f0-9c1a-0b9de33753ab&pf_rd_r=MGW0DV9GAWSKBZSRS5F4&qid=1677530606&s=apparel&sr=1-2-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ts_id=12035955011&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNM1YwUUcyTTBBUkEmZW5jcnlwdGVkSWQ9QTAxNTM1NjUxMjJYQk9aMUFXUDhMJmVuY3J5cHRlZEFkSWQ9QTA0ODY4OTYxSlA0WEdXQlpRNEdIJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title_element = soup2.find(id='productTitle')
title = (title_element.get_text().strip())

price_element = soup2.find(class_="a-price-whole")
price = price_element.get_text().strip()

print(title)
print(price)

title_element = soup2.find(id='productTitle')
title = (title_element.get_text().strip())
print(title)

price_element = soup2.find(class_="a-price-whole")
price = price_element.get_text().strip()
print(price)

price = price[:2]
price

ratings_element = soup2.find(class_="a-icon a-icon-star a-star-4-5")
ratings = ratings_element.get_text().strip()
print(ratings)

ratings = ratings[:3]
print(ratings)

ratings_count_element = soup2.find(id="acrCustomerReviewText")
ratings_count = ratings_count_element.get_text().strip()
print(ratings_count)

ratings_count = ratings_count[: -8]
print(ratings_count)

import datetime

today = datetime.date.today()
print(today)

import csv 

header =['title', 'price','date', 'number_of_ratings', 'ratings']
data = [title, price,today,ratings_count, ratings]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

import pandas as pd

df = pd.read_csv('AmazonWebScraperDataset.csv')
df

from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # Create a MIMEText object with the message body
    message = MIMEText(body)
    
    # Set the subject, sender, and recipient
    message['Subject'] = subject
    message['From'] = 'jillskillion@gmail.com'
    message['To'] = to_email
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login('jillskillion@gmail.com', 'xxxxxxxxxxxxxxxxx')
        smtp_server.sendmail('jillskillion@gmail.com', to_email, message.as_string())

# Example usage
subject = "The Shirt you want is below $14! Now is your chance to buy!"
body = "Osikanyi, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Morningwood-Offensive-Novelty-Graphic-Tees/dp/B00PJARZ7M/ref=sxin_16_pa_sp_search_thematic_sspa?c=ts&content-id=amzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab%3Aamzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab&cv_ct_cx=Novelty+Clothing+%26+More&keywords=Novelty+Clothing+%26+More&pd_rd_i=B00PJARZ7M&pd_rd_r=e972c888-7136-4bf3-80c6-2619b50f523d&pd_rd_w=Kyrm2&pd_rd_wg=E81dI&pf_rd_p=948775b6-578a-48f0-9c1a-0b9de33753ab&pf_rd_r=MGW0DV9GAWSKBZSRS5F4&qid=1677530606&s=apparel&sr=1-2-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ts_id=12035955011&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNM1YwUUcyTTBBUkEmZW5jcnlwdGVkSWQ9QTAxNTM1NjUxMjJYQk9aMUFXUDhMJmVuY3J5cHRlZEFkSWQ9QTA0ODY4OTYxSlA0WEdXQlpRNEdIJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
to_email = "jillskillion@gmail.com"
send_email(subject, body, to_email)


def check_price():
    URL = 'https://www.amazon.com/Morningwood-Offensive-Novelty-Graphic-Tees/dp/B00PJARZ7M/ref=sxin_16_pa_sp_search_thematic_sspa?c=ts&content-id=amzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab%3Aamzn1.sym.948775b6-578a-48f0-9c1a-0b9de33753ab&cv_ct_cx=Novelty+Clothing+%26+More&keywords=Novelty+Clothing+%26+More&pd_rd_i=B00PJARZ7M&pd_rd_r=e972c888-7136-4bf3-80c6-2619b50f523d&pd_rd_w=Kyrm2&pd_rd_wg=E81dI&pf_rd_p=948775b6-578a-48f0-9c1a-0b9de33753ab&pf_rd_r=MGW0DV9GAWSKBZSRS5F4&qid=1677530606&s=apparel&sr=1-2-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&ts_id=12035955011&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNM1YwUUcyTTBBUkEmZW5jcnlwdGVkSWQ9QTAxNTM1NjUxMjJYQk9aMUFXUDhMJmVuY3J5cHRlZEFkSWQ9QTA0ODY4OTYxSlA0WEdXQlpRNEdIJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title_element = soup2.find(id='productTitle')
    title = (title_element.get_text().strip())

    price_element = soup2.find(class_="a-price-whole")
    price = price_element.get_text().strip()
    price = price[:2]
    
    ratings_element = soup2.find(class_="a-icon a-icon-star a-star-4-5")
    ratings = ratings_element.get_text().strip()
    ratings = ratings[:3]
    
    ratings_count_element = soup2.find(id="acrCustomerReviewText")
    ratings_count = ratings_count_element.get_text().strip()
    ratings_count = ratings_count[: -8]
    
    import datetime
    today = datetime.date.today()
    
    import csv 
    header =['title', 'price','date', 'number_of_ratings', 'ratings']
    data = [title, price,today,ratings_count, ratings]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if (int(price)<14):
        send_email()

while(True):
    check_price()
    time.sleep(86400)

