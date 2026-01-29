# Web Scraping dhe API Integration Projekti

## Përshkrimi i Projektit
Ky projekt implementon web scraping nga Telegrafi.com dhe API integration nga Open-Meteo për të marrë të dhëna të lajmeve dhe motit.

## Teknologjitë e Përdorura
- Python 3.13
- Requests për kërkesa HTTP
- BeautifulSoup4 për web scraping
- JSON për ruajtjen e të dhënave

## Detaje të Të Dhënave

### Web Scraping nga Telegrafi.com
- **Skedari:** `scraping_telegrafi_fixed.py`
- **Output:** `telegrafi_lajmet.json`
- **P.S:** Telegrafi.com nuk shfaq datën e artikujve në faqen kryesore, prandaj fusha "data" mund të jetë bosh. Artikulli i parë është një kategori e veçantë e faqes.

### API Integration me Open-Meteo
- **Skedari:** `api_open_meteo.py`
- **Output:** `moti_tirane.json`
- **API:** Open-Meteo (falas, pa authentication)

### Kombinimi i Të Dhënave
- **Skedari:** `combine_data.py`
- **Output:** `combined_data.json`
- **Funksioni:** Bashkon lajmet nga Telegrafi me të dhënat e motit nga API


## Ekzekutimi
1. Instalo libraritë: `pip install -r requirements.txt`
2. Ekzekuto web scraping: `python scraping_telegrafi_fixed.py`
3. Ekzekuto API integration: `python api_open_meteo.py`
4. Ekzekuto kombinimin: `python combine_data.py`

