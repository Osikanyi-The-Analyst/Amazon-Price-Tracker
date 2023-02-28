# 🕸️ Amazon Price Tracker
This project is a Python script that allows you to monitor the price of a certain product on Amazon and receive email alerts when there is a sudden reduction in price. This can be especially useful during Black Friday sales or other promotions where prices are likely to fluctuate.

## 🚀 How it Works
The script uses the BeautifulSoup and Requests libraries to scrape the product page on Amazon and extract the price information. It then compares the current price to a target price that you set and sends an email notification if the current price drops below the target price.

## 🤔 Getting Started
To use this project, you will need to have Python 3.x installed on your computer. You will also need to install the BeautifulSoup and Requests libraries by running the following command:

pip install beautifulsoup4 requests

Next, you will need to configure the script by setting the following variables:

**URL: The URL of the product page on Amazon that you want to track.
**TARGET_PRICE: The target price that you want to be alerted when the product drops below.
**FROM_EMAIL: The email address that the notification will be sent from.
**FROM_EMAIL_PASSWORD: The password for the email address that the notification will be sent from.
**TO_EMAIL: The email address that the notification will be sent to.
**Once you have configured the script, you can run it by navigating to the directory containing the script and running the following command:

_python amazon_price_tracker.py_

## 📝 Conclusion
This project demonstrates how Python can be used for web scraping and automation. It can be useful for anyone who wants to monitor the price of a product on Amazon and receive notifications when the price drops below a certain threshold. Feel free to use this project as a starting point for your own Amazon price tracking tool, and don't forget to star the repository if you find it useful!

## 🙏 Acknowledgments
Thank you to the developers of BeautifulSoup and requests for making this project possible.
