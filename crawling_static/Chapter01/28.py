from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.yahoo.com/most-active"
res = req.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
})
soup = BS(res.text, "html.parser")
print(soup)
#for tr in soup.select("table tbody tr"):
    #title = tr.select("td:nth-child(1)")[0].get_text(strip=True)
    #price = tr.select("td:nth-child(3) fin-streamer")[0].get_text(strip=True)
    #change = tr.select("td:nth-child(5)")[0].get_text(strip=True)
    #print(title, price, change)

# 막힌듯 함
# <h1 style="margin-top:20px;">Will be right back...</h1>
#<p id="message-1">Thank you for your patience.</p>
#<p id="message-2">Our engineers are working quickly to resolve the issue.</p>
