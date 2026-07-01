import feedparser
from clean_html import clean_html
import random



def run_line(type:int):
    bad_words = ["<p>", "</p>", "&nbsp;", "\xa0"]
    data = {}

    if type == 1:
        url = "https://habr.com/ru/rss/best/" 
    elif type == 2:
        url = "https://habr.com/ru/rss/hub/programming/"
    elif type == 3:
        url = "https://habr.com/ru/rss/hub/electronics/"
    elif type == 4:
        url = "https://habr.com/ru/rss/hub/diy/"
    elif type == 5:
        url = "https://habr.com/ru/rss/hub/hardware/"
    elif type == 6:
        urls = [
            "https://habr.com/ru/rss/best/",
            "https://habr.com/ru/rss/hub/programming/",
            "https://habr.com/ru/rss/hub/electronics/",
            "https://habr.com/ru/rss/hub/diy/",
            "https://habr.com/ru/rss/hub/hardware/"
            ]

        for i in range(5):
            feed = feedparser.parse(urls[i])
            j = 0
            for entry in feed.entries[:5]:   # берём 5 последних
                j+=1
                text = entry.summary if hasattr(entry, 'summary') else entry.description if hasattr(entry, 'description') else ""
                for word in bad_words:
                    text = text.replace(word, "")
                    text = text.replace(word.capitalize(), "")
                clean_text = clean_html(text)
                
                data[f"title{i+1}{j}"] = entry.title           # заголовок
                data[f"text{i+1}{j}"] = clean_text             # содержание
                data[f"date{i+1}{j}"] = entry.published        # дата


    if type != 6:
        feed = feedparser.parse(url)
        
        i = 0
        for entry in feed.entries[:5]:   # берём 5 последних
            i+=1
            text = entry.summary if hasattr(entry, 'summary') else entry.description if hasattr(entry, 'description') else ""
            for word in bad_words:
                text = text.replace(word, "")
                text = text.replace(word.capitalize(), "")
            clean_text = clean_html(text)
            
            data[f"title{i}"] = entry.title           # заголовок
            data[f"text{i}"] = clean_text             # содержание
            data[f"date{i}"] = entry.published        # дата

    return data

data = run_line(6)
print(data)