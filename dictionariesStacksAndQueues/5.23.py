import json
import requests

url = "https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"

data = requests.get(url, timeout=10).json()

with open("euro.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved to euro.json\n")

with open("euro.json", "r", encoding="utf-8") as f:
    euro = json.load(f)

print("Date           Buying Rate     Selling Rate")
print("===========================================")

for rate in euro["rates"]:
    date = rate["effectiveDate"]
    buying = f'{rate["bid"]:.4f}'
    selling = f'{rate["ask"]:.4f}'
    print(f"{date}     {buying:<12}  {selling:<12}")