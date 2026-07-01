from bs4 import BeautifulSoup

def clean_html(text):
    if not text:
        return text
    
    # Убираем весь HTML
    soup = BeautifulSoup(text, 'html.parser')
    
    # Удаляем все картинки
    for img in soup.find_all('img'):
        img.decompose()          # полностью удаляет тег
    
    # Удаляем все ссылки, но оставляем текст внутри них
    for a in soup.find_all('a'):
        a.replace_with(a.get_text())   # заменяем ссылку на чистый текст
    
    # Получаем чистый текст
    clean_text = soup.get_text()
    
    # Дополнительная очистка
    clean_text = clean_text.strip()
    clean_text = " ".join(clean_text.split())  # убираем лишние пробелы и переносы
    
    return clean_text