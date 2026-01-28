import requests
from bs4 import BeautifulSoup
import json

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

        for artikull in artikujt[:10]:
            titull_element = artikull.find('h2')

            if titull_element:
                titulli = titull_element.text.strip()

                data_element = artikull.find('time')
                data = data_element['datetime'] if data_element and data_element.has_attr('datetime') else ''

                link_element = artikull.find('a')
                link = link_element['href'] if link_element and link_element.has_attr('href') else ''

                if link and not link.startswith('http'):
                    link = 'https://telegrafi.com' + link

                lajmet.append({
                    'titulli': titulli,
                    'data': data,
                    'linku': link,
                    'burimi': 'Telegrafi.com'
                })

        with open('telegrafi_lajmet.json', 'w', encoding='utf-8') as f:
            json.dump(lajmet, f, indent=2, ensure_ascii=False)

        print(f"U ruajten {len(lajmet)} lajme ne telegrafi_lajmet.json")

        print("\nLajmet e marra:")
        for i, lajm in enumerate(lajmet[:3], 1):
            print(f"{i}. {lajm['titulli'][:80]}...")

    else:
        print(f"Gabim: Status code {response.status_code}")

except requests.exceptions.Timeout:
    print("Lidhja u ndal pas 10 sekondash")
except requests.exceptions.ConnectionError:
    print("Problem me lidhjen e internetit")
except Exception as e:
    print(f"Gabim: {e}")