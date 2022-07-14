import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

EMAIL = ""
PASSWORD = ""

url = "https://www.amazon.co.uk/Govee-Backlights-Camera-Google-Assistant/dp/B095W4XRWS/ref=sxin_14?content-id=amzn1" \
      ".sym.0fc07935-f7c6-4751-9a61-01858a9c7291%3Aamzn1.sym.0fc07935-f7c6-4751-9a61-01858a9c7291&crid=267ZK8SKI66LA" \
      "&cv_ct_cx=led+bars&keywords=led+bars&pd_rd_i=B095W4XRWS&pd_rd_r=b8576936-1cb1-49c3-a90d-1856243f220c&pd_rd_w" \
      "=6RUZd&pd_rd_wg=2vldU&pf_rd_p=0fc07935-f7c6-4751-9a61-01858a9c7291&pf_rd_r=9GBTVTFBWTV606CCX6QX&qid=1657715958" \
      "&smid=AI0ZYPYC3AQ9C&sprefix=led+bars%2Caps%2C61&sr=1-2-b8003e8c-7dbe-4d7b-b373-a406a41b9947"

header = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(url, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.content, "lxml")
amazon_price = soup.find(name="span", class_="a-offscreen").getText().split("£")
price = float(amazon_price[1])

if price < 35:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="",
                            msg=f"Subject:LED Bar\n\nThis product is now only {price}.")
