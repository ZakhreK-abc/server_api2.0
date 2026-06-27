import requests
from bs4 import BeautifulSoup

def weather():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        r = requests.get("https://yandex.ru/pogoda/chelyabinsk", 
                        headers=headers, timeout=20)
        print("Статус:", r.status_code)
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        temp = (soup.find('span', {'class': lambda x: x and 'temp' in x}))
        cond = (soup.find('span', {'class': lambda x: x and 'warning__first_text' in x}))
        items = soup.find_all('li', class_='AppFact_details__item__QFIXI')[:4]
        data = {}
        
        if temp:
            data['temp'] = temp.get_text().strip()
        else:
            data['temp'] = None


        if cond:
            data['cond'] = cond.get_text().strip()
        else:
            data['cond'] = None


        if items:
            data['wind'] = items[0].get_text().strip()
            data['pressure'] = items[1].get_text().strip() + ' мм'
            data['humidity'] = items[2].get_text().strip()
            data['feels_like'] = items[3].get_text().strip()
        
        else:
            data['wind'] = None
            data['pressure'] = None
            data['humidity'] = None
            data['feels_like'] = None
 
    except Exception as e:
        raise RuntimeError("Ошибка:", e)
    
    return data
