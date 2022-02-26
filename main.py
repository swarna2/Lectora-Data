from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://revistes.ub.edu/index.php/lectora/article/view/33277').text
soup = BeautifulSoup(html_text, 'lxml')
Title = soup.find('h1', class_='page_title').text
Author = soup.find('span', class_='name').text.replace(' ', '')
Values = soup.find('section', class_='item keywords')
Keywords = Values.find('span', class_='value').text.replace(' ', '')
Abstract = soup.find('p').text
Issue_Number = soup.find('a', class_='title').text.replace(' ', '')
with open(f'posts/Data.txt', 'w') as f:
    f.write(f"Title: {Title.strip()} \n")
    f.write(f"Author: {Author.strip()} \n")
    f.write(f"Keywords: {Keywords.strip()} \n")
    f.write(f"Abstract: {Abstract.strip()} \n")
    f.write(f"Issue Number: {Issue_Number.strip()} \n")

