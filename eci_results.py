import requests
from bs4 import BeautifulSoup

url = "https://results.eci.gov.in/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

main_content = soup.find('main', class_='inner-content')

parliamentary_constituencies = None
if main_content:
    parliamentary_section = main_content.find('div', class_='pc-wrap')
    if parliamentary_section:
        parliamentary_constituencies = parliamentary_section.find('h1').text.strip()

counts = []
state_items = main_content.find_all('div', class_='state-item') if main_content else []
for item in state_items:
    state_name = ' '.join(item.find('h2').text.split())
    constituency_count = item.find('h1').text.strip()
    counts.append((state_name, constituency_count))

buttons = main_content.find_all('a', class_='btn-big') if main_content else []
for button in buttons:
    state_name = button.text.strip()
    counts.append((state_name, None))

if parliamentary_constituencies:
    print(f"Parliamentary Constituencies: {parliamentary_constituencies}")

print("\nAssembly Constituencies:")
for state, count in counts:
    print(f"{state}: {count if count else 'No count provided'}")
