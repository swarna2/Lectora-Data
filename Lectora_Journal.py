from bs4 import BeautifulSoup
import requests

urls = ['https://revistes.ub.edu/index.php/lectora/article/view/33302',
       'https://revistes.ub.edu/index.php/lectora/article/view/33044',
       'https://revistes.ub.edu/index.php/lectora/article/view/33063']
Title_List = []
Author_List = []
Keywords_List = []
Abstract_List = []
Issue_Number_List = []
for url in urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    Title = soup.find('h1', class_='page_title').text
    Title_List.append(Title)
    Author = soup.find('span', class_='name').text.replace(' ', '')
    Author_List.append(Author)
    Values = soup.find('section', class_='item keywords')
    Keywords = Values.find('span', class_='value').text.replace(' ', '')
    Keywords_List.append(Keywords)
    Abstract = soup.find('p').text
    Abstract_List.append(Abstract)
    Issue_Number = soup.find('a', class_='title').text.replace(' ', '')
    Issue_Number_List.append(Issue_Number)
with open(f'posts/Data.txt', 'w') as f:
    for items in Title_List:
        f.write('\nTitle: %s' % items)
    for items in Author_List:
        f.write('\nAuthor: %s' % items)
    for items in Keywords_List:
        f.write('\nKeywords: %s' % items)
    for items in Abstract_List:
        f.write('\nAbstract: %s' % items)
    for items in Issue_Number_List:
        f.write('\nIssue_Number: %s' % items)
