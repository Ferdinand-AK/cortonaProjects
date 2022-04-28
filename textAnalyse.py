from itertools import count
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

link = "https://de.wikipedia.org/wiki/Formel_1"

html = requests.get(link).text

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

text = text_from_html(html)

print(text)
