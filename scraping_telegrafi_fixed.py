import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

print("HAPI 1: SCRAPING NGA TELEGRAFI.COM")
print("=" * 50)

url = "https://telegrafi.com"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        print("U lidh me telegrafi.com")

        soup = BeautifulSoup(response.content, 'html.parser')

        artikujt = soup.find_all('article')
        print(f"U gjeten {len(artikujt)} artikuj")

        lajmet = []

        for artikull in artikujt[:15]:
            titull_element = artikull.find('h2')

            if titull_element:
                titulli = titull_element.text.strip()

                data_element = artikull.find('time')
                if data_element:
                    if data_element.has_attr('datetime'):
                        data = data_element['datetime']
                    else:
                        data = data_element.text.strip()
                else:
                    span_koha = artikull.find('span', class_='time')
                    if span_koha:
                        data = span_koha.text.strip()
                    else:
                        data = datetime.now().strftime("%Y-%m-%d")

                link_element = artikull.find('a')
                link = link_element['href'] if link_element and link_element.has_attr('href') else ''

                if link and not link.startswith('http'):
                    link = 'https://telegrafi.com' + link

                kategori_element = artikull.find('span', class_='category')
                kategori = kategori_element.text.strip() if kategori_element else 'Lajme'

                lajmet.append({
                    'titulli': titulli,
                    'data': data,
                    'linku': link,
                    'kategoria': kategori,
                    'burimi': 'Telegrafi.com',
                    'data_marrjes': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

        with open('telegrafi_lajmet.json', 'w', encoding='utf-8') as f:
            json.dump(lajmet, f, indent=2, ensure_ascii=False)

        print(f"U ruajten {len(lajmet)} lajme ne telegrafi_lajmet.json")

        print("\nLajmet e marra (me date):")
        for i, lajm in enumerate(lajmet[:3], 1):
            data_shfaq = lajm['data'] if lajm['data'] else 'Pa date'
            print(f"{i}. [{data_shfaq}] {lajm['titulli'][:60]}...")

    else:
        print(f"Gabim: Status code {response.status_code}")

except Exception as e:
    print(f"Gabim: {e}")