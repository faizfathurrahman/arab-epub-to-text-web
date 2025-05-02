from ebooklib import epub
from ebooklib import ITEM_DOCUMENT
from bs4 import BeautifulSoup

def extract_text_from_epub(file_path):
    book = epub.read_epub(file_path)
    text = ''
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text(separator='\n')
    return text
