import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/ONEPLUS-Wireless-IP55-rated-Resistance-Playtime/dp/B09YWBVMNM/ref=sr_1_6?currency=USD&keywords=oneplus%2Bbuds%2Bpro%2B2&qid=1677170172&sprefix=onplus%2B%2Caps%2C667&sr=8-6&th=1ONEPLUS-Wireless-IP55-rated-Resistance-Playtime%2Fdp%2FB09YWBVMNM%2Fref&language=en_US "
headers = {"Content-Type":"text" , 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                        ,"Accept-Language":"en-US,en;q=0.9"
                        }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span" , class_="a-price-whole").get_text()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user='gaurajrakholiya@gmail.com',password='vrixktttpelxkmxh')
        connection.sendmail(
            from_addr="gaurajrakholiya@gmail.com",
            to_addrs="gaurajrakholiya@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

        # https://www.123formbuilder.com/docs/setting-up-smtp-with-2-step-verification-on/