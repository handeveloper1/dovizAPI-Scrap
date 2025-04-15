import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://www.doviz.com/api/v1/golds/all/latest"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')


data = {}


items = soup.find_all('span', class_='name')

for item in items:
    name = item.text.strip()
    value = item.find_next('span', class_='value').text.strip()
    change_rate = item.find_next('div', class_='change-rate').text.strip()
    change_amount = item.find_next('div', class_='change-amount').text.strip()

    data[name] = {
        'value': value,
        'change_rate': change_rate,
        'change_amount': change_amount
    }


for name, info in data.items():
    print(f"Ürün: {name}")
    print(f"Değer: {info['value']}")
    print(f"Değişim Oranı: {info['change_rate']}")
    print(f"Artış Miktarı: {info['change_amount']}")
    print("-" * 50)
