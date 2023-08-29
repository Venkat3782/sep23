import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/tyy/4io/~cs-xj7gdemumj/pr?sid=tyy,4io&collection-tab-name=Redmi+Note+12+Pro+5G&param=6765363&otracker=clp_banner_1_14.bannerX3.BANNER_mobile-phones-big-saving-days-jan23-56hj-store_FMM4NVEBNJK7&fm=neo%2Fmerchandising&iid=M_1759d3b9-b177-460f-8912-e2ef29043ab2_14.FMM4NVEBNJK7&ppt=hp&ppn=homepage&ssid=ifyq0spp5d715dds1678817793060")
print(response)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
names = soup.find_all("div", class_="_4rR01T")
print(names)
name = []
for i in names[0:10]:
    d = i.get_text()
    name.append(d)


prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
price = []
for i in prices[0:10]:
    d = i.get_text()
    price.append(d)

ratings = soup.find_all("div", class_="_3LWZlK")
star = []
for i in ratings[0:10]:
    d = i.get_text()
    star.append(float(d))
print(star)

df = pandas.DataFrame()
df["Names"] = name
df["prices"] = price
df["ratings"] = star
df.to_csv("mobiles.csv")
