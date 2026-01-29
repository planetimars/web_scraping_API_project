import json

with open('telegrafi_lajmet.json', 'r') as f:
    lajmet = json.load(f)

with open('moti_tirane.json', 'r') as f:
    moti = json.load(f)

combined = {
    'lajmet': lajmet,
    'moti': moti,
    'info': 'Kombinuar nga web scraping dhe API'
}

with open('combined_data.json', 'w', encoding='utf-8') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)

print(f"U kombinuan {len(lajmet)} lajme me te dhenat e motit")