
import requests, re, time
from bs4 import BeautifulSoup

elements = []
length = 28

for i in range(1, 2):
    url = f'https://szotar.com/szokereso/hossz/{length}-betus/{i}'
    req = requests.get(url=url)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')
    for y in soup.find_all(href=re.compile("#")):
        elements.append(y)
    print(f'A(z) {i}. oldal leszedve..')
    time.sleep(0.2)

#print(elements)
f = open(f'{length}betus.txt', 'w', encoding='utf-8')
for a in elements:
    f.write(f'{a}\n')
f.close()