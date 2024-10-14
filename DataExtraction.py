from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import pandas as pd

def tag_visible(element):    
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'a', 'span', 'ul', 'ol', 'p[tdm-descr]']:
        return False
    if isinstance(element, Comment):
        return False
    if element.parent.name in ['p', 'h1']:
        return True
    return False

def text_from_html(body):
    soup = BeautifulSoup(body)
    texts = soup.article.findAll(string=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

df = pd.read_excel(r"D:/Job Hunt/Theta Academy/Python assignment/assignments/text analytics/Input.xlsx")
for i in range(len(df)):
    text_file_name = str(int(df['URL_ID'][i]))

    URL = df['URL'][i]
    # print(URL)
    response = requests.get(URL,headers=headers, cookies={'cookies':''})
    article_text = text_from_html(response.text)
    # print(article_text)

    ### creating text file with URL_ID as name containing title and text from the article on the URL ### 
    with open(r'D:/Job Hunt/Theta Academy/Python assignment/assignments/text analytics/DataExtracted/'+text_file_name+".txt", 'w', encoding="utf-8") as file: 
        file.write(article_text)

